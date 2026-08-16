import torch
import random
import numpy as np
import re
import faiss
import argparse
import json
from pathlib import Path
from datetime import datetime

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to the experiment configuration JSON file.",
    )
    return parser.parse_args()

def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    required_parameters = {
        "embedding_model",
        "model_name",
        "num_questions",
        "num_documents",
        "top_k_values",
        "seed",
        "index_file",
        "results_file",
    }
    missing_parameters = required_parameters - config.keys()

    if missing_parameters:
        missing = ", ".join(sorted(missing_parameters))
        raise ValueError(f"Missing configuration parameters: {missing}")

    top_k_values = config["top_k_values"]
    if (
        not isinstance(top_k_values, list)
        or not top_k_values
        or any(not isinstance(k, int) or k <= 0 for k in top_k_values)
    ):
        raise ValueError("top_k_values must be a non-empty list of positive integers.")

    config["top_k_values"] = sorted(set(top_k_values))

    return config

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    torch.use_deterministic_algorithms(True)
    torch.backends.cudnn.benchmark = False

def load_textbook_corpus(n, dataset):
    corpus = dataset["train"]

    if n is not None:
        if n <= 0:
            raise ValueError("NUM_DOCUMENTS must be greater than zero or None.")
        corpus = corpus.select(range(min(n, len(corpus))))

    return corpus

def load_evaluation_questions(n, dataset):
    evaluation_dataset = dataset["validation"]

    if n is not None:
        if n <= 0:
            raise ValueError("NUM_QUESTIONS must be greater than zero or None.")
        evaluation_dataset = evaluation_dataset.select(
            range(min(n, len(evaluation_dataset)))
        )

    return evaluation_dataset

def build_faiss_index(corpus, embedding_model):
    # Extract text from small corpus
    documents = corpus["content"]
    print("\nExample document:")
    print(documents[0])

    # Embed all textbook chunks
    print("\nEmbedding documents...")

    document_embeddings = embedding_model.encode(
        documents,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    print("\nEmbedding shape:")
    print(document_embeddings.shape)

    # Build FAISS index
    embedding_dimension = document_embeddings.shape[1]

    index = faiss.IndexFlatIP(embedding_dimension)
    index.add(document_embeddings)
    print(f"\nFAISS contains {index.ntotal} vectors.")

    return index

def load_or_build_faiss_index(
    index_file,
    corpus,
    embedding_model,
    embedding_model_name,
    num_documents,
):
    index_path = Path(index_file)
    metadata_path = Path(f"{index_file}.metadata.json")
    expected_metadata = {
        "embedding_model": embedding_model_name,
        "num_documents": num_documents,
        "corpus_size": len(corpus),
        "corpus_fingerprint": getattr(corpus, "_fingerprint", None),
        "normalize_embeddings": True,
    }

    if index_path.exists() and metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as file:
            saved_metadata = json.load(file)

        if saved_metadata == expected_metadata:
            print(f"Loading existing FAISS index from {index_path}...")
            index = faiss.read_index(str(index_path))

            if index.ntotal != len(corpus):
                raise ValueError(
                    f"The FAISS index contains {index.ntotal} vectors, "
                    f"but the selected corpus contains {len(corpus)} chunks."
                )

            print(f"FAISS contains {index.ntotal} vectors.")
            return index

        print("FAISS index settings changed. Rebuilding the index...")
    elif index_path.exists():
        print("FAISS index metadata is missing. Rebuilding the index...")
    else:
        print("No existing FAISS index found. Building the index...")

    index = build_faiss_index(corpus, embedding_model)

    index_path.parent.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(index_path))
    with open(metadata_path, "w", encoding="utf-8") as file:
        json.dump(expected_metadata, file, indent=2)

    print(f"FAISS index saved to {index_path}.")
    return index

def retrieve_documents(query, index, corpus, embedding_model, k=5):
    query_embedding = embedding_model.encode([query], normalize_embeddings=True)
    similarities, indices = index.search(query_embedding, k)
    retrieved_documents = []

    for similarity, index_id in zip(similarities[0], indices[0]):
        retrieved_documents.append(
            {
                "similarity": float(similarity),
                "document": corpus[int(index_id)],
            }
        )

    return retrieved_documents

def load_qwen(model_name):
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
    )
    model.eval()
    print("Model loaded.")
    return tokenizer, model


def build_question_prompt(example):
    return (
        "Question:\n"
        f"{example['question']}\n\n"
        f"A. {example['opa']}\n"
        f"B. {example['opb']}\n"
        f"C. {example['opc']}\n"
        f"D. {example['opd']}\n\n"
        "Answer with only one letter: A, B, C, or D."
    )


def build_rag_prompt(example, retrieved_documents):
    context = "\n\n".join(
        result["document"]["content"]
        for result in retrieved_documents
    )

    return (
        "Use the textbook context below to answer the multiple-choice question.\n\n"
        f"Context:\n{context}\n\n"
        f"{build_question_prompt(example)}"
    )

def ask_model(prompt, tokenizer, model):
    messages = [
        {
            "role": "system",
            "content": "You are a medical question answering assistant.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    model_inputs = tokenizer(
        text,
        return_tensors="pt",
    ).to(model.device)

    with torch.inference_mode():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=5,
            do_sample=False,
        )

    generated_ids = generated_ids[
        :, model_inputs.input_ids.shape[1]:
    ]

    answer = tokenizer.batch_decode(
        generated_ids,
        skip_special_tokens=True,
    )[0]

    return answer.strip()

def extract_answer_letter(answer):
    match = re.search(r"\b[A-D]\b", answer.upper())
    return match.group(0) if match else None

def convert_correct_answer(cop):
    mapping = {0: "A", 1: "B", 2: "C", 3: "D"}
    return mapping[cop]

def evaluate_qwen_and_rag(
    evaluation_dataset,
    index,
    corpus,
    embedding_model,
    tokenizer,
    model,
    k_values,
):
    baseline_correct = 0
    rag_counts = {
        k: {
            "correct": 0,
            "fixed_answers": 0,
            "broke_answers": 0,
        }
        for k in k_values
    }
    total_questions = len(evaluation_dataset)
    max_k = max(k_values)

    for i, example in enumerate(evaluation_dataset):
        baseline_prompt = build_question_prompt(example)
        baseline_answer = ask_model(baseline_prompt, tokenizer, model)
        baseline_prediction = extract_answer_letter(baseline_answer)
        correct_answer = convert_correct_answer(example["cop"])
        baseline_is_correct = baseline_prediction == correct_answer

        if baseline_is_correct:
            baseline_correct += 1

        retrieved_documents = retrieve_documents(
            baseline_prompt,
            index,
            corpus,
            embedding_model,
            k=max_k,
        )
        rag_predictions = {}

        for k in k_values:
            rag_prompt = build_rag_prompt(example, retrieved_documents[:k])
            rag_answer = ask_model(rag_prompt, tokenizer, model)
            rag_prediction = extract_answer_letter(rag_answer)
            rag_predictions[k] = rag_prediction
            rag_is_correct = rag_prediction == correct_answer

            if rag_is_correct:
                rag_counts[k]["correct"] += 1

            if not baseline_is_correct and rag_is_correct:
                rag_counts[k]["fixed_answers"] += 1

            if baseline_is_correct and not rag_is_correct:
                rag_counts[k]["broke_answers"] += 1

        rag_progress = ", ".join(
            f"RAG(k={k})={rag_predictions[k]!r}"
            for k in k_values
        )

        print(
            f"{i + 1:04d}/{total_questions}: "
            f"Qwen={baseline_prediction!r}, "
            f"{rag_progress}, "
            f"expected={correct_answer!r}"
        )

    baseline_accuracy = baseline_correct / total_questions
    rag_results = {}

    for k in k_values:
        rag_accuracy = rag_counts[k]["correct"] / total_questions
        rag_results[str(k)] = {
            "correct": rag_counts[k]["correct"],
            "accuracy": rag_accuracy,
            "accuracy_difference": rag_accuracy - baseline_accuracy,
            "fixed_answers": rag_counts[k]["fixed_answers"],
            "broke_answers": rag_counts[k]["broke_answers"],
        }

    print("\n----------------------------")
    print("COMPARISON RESULTS")
    print("----------------------------")
    print(f"Questions:     {total_questions}")
    print(f"Qwen correct:  {baseline_correct}")
    print(f"Qwen accuracy: {baseline_accuracy:.2%}")

    for k in k_values:
        result = rag_results[str(k)]
        print(f"\nRAG k={k}")
        print(f"Correct:             {result['correct']}")
        print(f"Accuracy:            {result['accuracy']:.2%}")
        print(f"Accuracy difference: {result['accuracy_difference']:.2%}")
        print(f"Fixed answers:       {result['fixed_answers']}")
        print(f"Broke answers:       {result['broke_answers']}")

    return {
        "questions": total_questions,
        "qwen_correct": baseline_correct,
        "qwen_accuracy": baseline_accuracy,
        "rag_by_k": rag_results,
    }

def save_results_to_txt(results, config):
    text_results_file = Path(config["results_file"]).with_suffix(".txt")

    with open(text_results_file, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write(f"RUN TIME: {results['run_time']}\n\n")
        file.write("EXPERIMENT PARAMETERS\n")
        file.write("----------------------------\n")
        for parameter, value in config.items():
            file.write(f"{parameter}: {value}\n")

        file.write("\nCOMPARISON RESULTS\n")
        file.write("----------------------------\n")
        file.write(f"Questions:           {results['questions']}\n")
        file.write(f"Qwen correct:        {results['qwen_correct']}\n")
        file.write(f"Qwen accuracy:       {results['qwen_accuracy']:.2%}\n")

        for k, result in results["rag_by_k"].items():
            file.write(f"\nRAG k={k}\n")
            file.write(f"Correct:             {result['correct']}\n")
            file.write(f"Accuracy:            {result['accuracy']:.2%}\n")
            file.write(
                f"Accuracy difference: {result['accuracy_difference']:.2%}\n"
            )
            file.write(f"Fixed answers:       {result['fixed_answers']}\n")
            file.write(f"Broke answers:       {result['broke_answers']}\n")

    return text_results_file

def save_results_to_json(results, results_file):
    results_path = Path(results_file)

    if results_path.exists():
        with open(results_path, "r", encoding="utf-8") as file:
            previous_results = json.load(file)

        if not isinstance(previous_results, list):
            previous_results = [previous_results]
    else:
        previous_results = []

    previous_results.append(results)

    with open(results_path, "w", encoding="utf-8") as file:
        json.dump(previous_results, file, indent=2)

def main(config):
    set_seed(config["seed"])

    textbook_dataset = load_dataset("MedRAG/textbooks")
    corpus = load_textbook_corpus(config["num_documents"], textbook_dataset)

    embedding_model = SentenceTransformer(config["embedding_model"])
    index = load_or_build_faiss_index(
        config["index_file"],
        corpus,
        embedding_model,
        config["embedding_model"],
        config["num_documents"],
    )

    tokenizer, model = load_qwen(config["model_name"])

    medmcqa = load_dataset("openlifescienceai/medmcqa")
    evaluation_dataset = load_evaluation_questions(
        config["num_questions"],
        medmcqa,
    )

    results = evaluate_qwen_and_rag(
        evaluation_dataset,
        index,
        corpus,
        embedding_model,
        tokenizer,
        model,
        k_values=config["top_k_values"],
    )

    results["run_time"] = datetime.now().astimezone().isoformat()
    results["config"] = config

    text_results_file = save_results_to_txt(results, config)
    save_results_to_json(results, config["results_file"])

    print(f"Results saved to {config['results_file']}")
    print(f"Text report saved to {text_results_file}")

if __name__ == "__main__":
    arguments = parse_arguments()
    experiment_config = load_config(arguments.config)
    main(experiment_config)
