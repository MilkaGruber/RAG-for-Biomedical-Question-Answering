import torch
import random
import numpy as np
import re
import faiss
import argparse
import json
import hashlib
from pathlib import Path
from datetime import datetime

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

SYSTEM_PROMPT = "You are a medical question answering assistant."
MAX_NEW_TOKENS = 5

def parse_arguments():
    # determines which configuration file with parameters to choose
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
        "question_only",
        "document_field",
        "max_input_tokens",
        "baseline_cache_file",
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

    if not isinstance(config["question_only"], bool):
        raise ValueError("question_only must be true or false.")

    if config["document_field"] not in {"content", "contents"}:
        raise ValueError("document_field must be either 'content' or 'contents'.")

    if (
        not isinstance(config["max_input_tokens"], int)
        or config["max_input_tokens"] <= MAX_NEW_TOKENS
    ):
        raise ValueError(
            f"max_input_tokens must be an integer greater than {MAX_NEW_TOKENS}."
        )

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

def load_evaluation_questions(n, dataset, seed):
    evaluation_dataset = dataset["validation"]

    if n is not None:
        if n <= 0:
            raise ValueError("NUM_QUESTIONS must be greater than zero or None.")
        evaluation_dataset = evaluation_dataset.shuffle(seed=seed).select(
            range(min(n, len(evaluation_dataset)))
        )

    return evaluation_dataset

def build_faiss_index(corpus, embedding_model, document_field):
    # this will return the embeddings of the data chunks
    # + an efficient search operation (k closest vectors)
    # Extract text from corpus
    documents = corpus[document_field]
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
    document_field,
):

    index_path = Path(index_file)
    metadata_path = Path(f"{index_file}.metadata.json")
    expected_metadata = {
        "embedding_model": embedding_model_name,
        "num_documents": num_documents,
        "corpus_size": len(corpus),
        "corpus_fingerprint": getattr(corpus, "_fingerprint", None),
        "normalize_embeddings": True,
        "document_field": document_field,
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

    index = build_faiss_index(corpus, embedding_model, document_field)

    index_path.parent.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(index_path))
    with open(metadata_path, "w", encoding="utf-8") as file:
        json.dump(expected_metadata, file, indent=2)

    print(f"FAISS index saved to {index_path}.")
    return index

def retrieve_documents(query, index, corpus, embedding_model, k=5):
    if k > len(corpus):
        raise ValueError(
            f"Cannot retrieve k={k} documents from a corpus of {len(corpus)} chunks."
        )

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


def embedding_specific_index_file(index_file, embedding_model_name, document_field):
    """Keep independently reusable indexes for different embedding configurations."""
    index_path = Path(index_file)
    model_tag = re.sub(r"[^A-Za-z0-9._-]+", "_", embedding_model_name)
    suffix = index_path.suffix or ".index"
    return str(
        index_path.with_name(
            f"{index_path.stem}.{model_tag}.{document_field}{suffix}"
        )
    )


def model_specific_cache_file(cache_file, model_name):
    """Keep baseline predictions reusable when switching between LLMs."""
    cache_path = Path(cache_file)
    model_tag = re.sub(r"[^A-Za-z0-9._-]+", "_", model_name)
    suffix = cache_path.suffix or ".json"
    return str(cache_path.with_name(f"{cache_path.stem}.{model_tag}{suffix}"))

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


def build_retrieval_query(example, question_only=False):
    """Build a content-only query for semantic retrieval."""
    if question_only:
        return example["question"]

    return (
        f"{example['question']}\n"
        f"{example['opa']}\n"
        f"{example['opb']}\n"
        f"{example['opc']}\n"
        f"{example['opd']}"
    )


def build_rag_prompt(example, retrieved_documents):
    # Combines retrieved FAISS documents with the question to create a RAG prompt.
    context = "\n\n".join(
        result["document"]["content"] for result in retrieved_documents
    )

    return (
        "Use the textbook context below to answer the multiple-choice question.\n\n"
        f"Context:\n{context}\n\n"
        f"{build_question_prompt(example)}"
    )

def ask_model(prompt, tokenizer, model, max_input_tokens):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
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

    model_inputs = tokenizer(text, return_tensors="pt")
    input_token_count = model_inputs.input_ids.shape[1]

    if input_token_count + MAX_NEW_TOKENS > max_input_tokens:
        raise ValueError(
            f"Prompt has {input_token_count} input tokens, but the configured limit "
            f"is {max_input_tokens} including {MAX_NEW_TOKENS} generated tokens. "
            "Reduce k or increase max_input_tokens if the model supports it."
        )

    model_inputs = model_inputs.to(model.device)

    # because we're not training QWEN, we disable gradient calculation
    # # we're only generating the response
    with torch.inference_mode():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False,
        )

    # remove original promp tokens, so we're left with only LLM's response -> the letter
    generated_ids = generated_ids[:, model_inputs.input_ids.shape[1]:]

    answer = tokenizer.batch_decode(
        generated_ids,
        skip_special_tokens=True,
    )[0]

    return answer.strip(), input_token_count

def extract_answer_letter(answer):
    # we do a regex search, find the first standalone letter (A, B, C or D)
    match = re.search(r"\b[A-D]\b", answer.upper())
    return match.group(0) if match else None

def convert_correct_answer(cop):
    mapping = {0: "A", 1: "B", 2: "C", 3: "D"}
    return mapping[cop]


def question_signature(example):
    fields = ["question", "opa", "opb", "opc", "opd"]
    content = json.dumps(
        {field: example[field] for field in fields},
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_baseline_cache(cache_file, expected_metadata):
    cache_path = Path(cache_file)
    if not cache_path.exists():
        return {"metadata": expected_metadata, "predictions": {}}

    try:
        with open(cache_path, "r", encoding="utf-8") as file:
            cache = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Baseline cache could not be read. Starting a new cache.")
        return {"metadata": expected_metadata, "predictions": {}}

    if cache.get("metadata") != expected_metadata:
        print("Baseline cache settings changed. Starting a new cache.")
        return {"metadata": expected_metadata, "predictions": {}}

    return cache


def save_baseline_cache(cache, cache_file):
    cache_path = Path(cache_file)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_path, "w", encoding="utf-8") as file:
        json.dump(cache, file, indent=2, ensure_ascii=False)

def evaluate_qwen_and_rag(
    evaluation_dataset,
    index,
    corpus,
    embedding_model,
    tokenizer,
    model,
    k_values,
    question_only,
    model_name,
    max_input_tokens,
    baseline_cache_file,
):
    baseline_correct = 0
    baseline_invalid_answers = 0
    rag_counts = {
        k: {
            "correct": 0,
            "fixed_answers": 0,
            "broke_answers": 0,
            "invalid_answers": 0,
        }
        for k in k_values
    }
    total_questions = len(evaluation_dataset)
    if total_questions == 0:
        raise ValueError("The evaluation dataset is empty.")

    max_k = max(k_values)
    if max_k > len(corpus):
        raise ValueError(
            f"The largest k ({max_k}) exceeds the corpus size ({len(corpus)})."
        )

    cache_metadata = {
        "model_name": model_name,
        "system_prompt": SYSTEM_PROMPT,
        "question_prompt_version": 1,
        "max_new_tokens": MAX_NEW_TOKENS,
        "max_input_tokens": max_input_tokens,
    }
    baseline_cache = load_baseline_cache(baseline_cache_file, cache_metadata)
    evaluation_details = []

    for i, example in enumerate(evaluation_dataset):
        # RESULT RETURNED BY QWEN ONLY
        example_id = str(example["id"])
        signature = question_signature(example)
        cached_baseline = baseline_cache["predictions"].get(example_id)

        if cached_baseline and cached_baseline.get("question_signature") == signature:
            baseline_answer = cached_baseline["raw_answer"]
            baseline_prediction = cached_baseline["prediction"]
            baseline_input_tokens = cached_baseline["input_tokens"]
        else:
            baseline_prompt = build_question_prompt(example)
            baseline_answer, baseline_input_tokens = ask_model(
                baseline_prompt,
                tokenizer,
                model,
                max_input_tokens,
            )
            baseline_prediction = extract_answer_letter(baseline_answer)
            baseline_cache["predictions"][example_id] = {
                "question_signature": signature,
                "raw_answer": baseline_answer,
                "prediction": baseline_prediction,
                "input_tokens": baseline_input_tokens,
            }

            if (i + 1) % 25 == 0:
                save_baseline_cache(baseline_cache, baseline_cache_file)

        correct_answer = convert_correct_answer(example["cop"])
        baseline_is_correct = baseline_prediction == correct_answer

        if baseline_is_correct:
            baseline_correct += 1
        if baseline_prediction is None:
            baseline_invalid_answers += 1

        # RESULTS RETURNED BY QWEN + RAG
        retrieval_query = build_retrieval_query(example, question_only)
        retrieved_documents = retrieve_documents(
            retrieval_query,
            index,
            corpus,
            embedding_model,
            k=max_k,
        )
        rag_predictions = {}
        rag_details = {}

        for k in k_values:
            rag_prompt = build_rag_prompt(example, retrieved_documents[:k])
            rag_answer, rag_input_tokens = ask_model(
                rag_prompt,
                tokenizer,
                model,
                max_input_tokens,
            )
            rag_prediction = extract_answer_letter(rag_answer)
            rag_is_correct = rag_prediction == correct_answer
            rag_predictions[k] = rag_prediction
            rag_details[str(k)] = {
                "raw_answer": rag_answer,
                "prediction": rag_prediction,
                "input_tokens": rag_input_tokens,
                "is_correct": rag_is_correct,
                "outcome": (
                    "preserved_correct"
                    if baseline_is_correct and rag_is_correct
                    else "corrupted"
                    if baseline_is_correct
                    else "fixed"
                    if rag_is_correct
                    else "preserved_incorrect"
                ),
            }

            if rag_is_correct:
                rag_counts[k]["correct"] += 1

            if not baseline_is_correct and rag_is_correct:
                rag_counts[k]["fixed_answers"] += 1

            if baseline_is_correct and not rag_is_correct:
                rag_counts[k]["broke_answers"] += 1

            if rag_prediction is None:
                rag_counts[k]["invalid_answers"] += 1

        evaluation_details.append(
            {
                "question_id": example_id,
                "question": example["question"],
                "options": {
                    "A": example["opa"],
                    "B": example["opb"],
                    "C": example["opc"],
                    "D": example["opd"],
                },
                "expected": correct_answer,
                "subject_name": example.get("subject_name"),
                "topic_name": example.get("topic_name"),
                "dataset_explanation": example.get("exp"),
                "retrieval_query": retrieval_query,
                "baseline": {
                    "raw_answer": baseline_answer,
                    "prediction": baseline_prediction,
                    "input_tokens": baseline_input_tokens,
                    "is_correct": baseline_is_correct,
                },
                "retrieved_documents": [
                    {
                        "rank": rank,
                        "id": result["document"]["id"],
                        "title": result["document"]["title"],
                        "similarity": result["similarity"],
                        "content": result["document"]["content"],
                    }
                    for rank, result in enumerate(retrieved_documents, start=1)
                ],
                "rag_by_k": rag_details,
            }
        )

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

    save_baseline_cache(baseline_cache, baseline_cache_file)

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
            "invalid_answers": rag_counts[k]["invalid_answers"],
        }

    print("\n----------------------------")
    print("COMPARISON RESULTS")
    print("----------------------------")
    print(f"Questions:     {total_questions}")
    print(f"Qwen correct:  {baseline_correct}")
    print(f"Qwen accuracy: {baseline_accuracy:.2%}")
    print(f"Qwen invalid outputs: {baseline_invalid_answers}")

    for k in k_values:
        result = rag_results[str(k)]
        print(f"\nRAG k={k}")
        print(f"Correct:             {result['correct']}")
        print(f"Accuracy:            {result['accuracy']:.2%}")
        print(f"Accuracy difference: {result['accuracy_difference']:.2%}")
        print(f"Fixed answers:       {result['fixed_answers']}")
        print(f"Broke answers:       {result['broke_answers']}")
        print(f"Invalid outputs:     {result['invalid_answers']}")

    return {
        "questions": total_questions,
        "qwen_correct": baseline_correct,
        "qwen_accuracy": baseline_accuracy,
        "qwen_invalid_answers": baseline_invalid_answers,
        "rag_by_k": rag_results,
        "evaluation_details": evaluation_details,
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
        file.write(f"Qwen invalid outputs: {results['qwen_invalid_answers']}\n")

        for k, result in results["rag_by_k"].items():
            file.write(f"\nRAG k={k}\n")
            file.write(f"Correct:             {result['correct']}\n")
            file.write(f"Accuracy:            {result['accuracy']:.2%}\n")
            file.write(
                f"Accuracy difference: {result['accuracy_difference']:.2%}\n"
            )
            file.write(f"Fixed answers:       {result['fixed_answers']}\n")
            file.write(f"Broke answers:       {result['broke_answers']}\n")
            file.write(f"Invalid outputs:     {result['invalid_answers']}\n")

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


def markdown_cell(value):
    """Format a value safely for use inside a Markdown table cell."""
    if value is None:
        return "N/A"
    if isinstance(value, float):
        return f"{value:.2%}"
    return str(value).replace("|", "\\|").replace("\n", " ")


def save_results_to_markdown(results_file):
    """Create a readable Markdown companion containing every saved JSON run."""
    results_path = Path(results_file)
    with open(results_path, "r", encoding="utf-8") as file:
        saved_results = json.load(file)

    runs = saved_results if isinstance(saved_results, list) else [saved_results]
    lines = ["# RAG experiment results", ""]

    for run_number, run in enumerate(runs, start=1):
        lines.extend([
            f"## Run {run_number}", "",
            f"**Run time:** {run.get('run_time', 'unknown')}", "",
            "### Configuration", "",
            "| Parameter | Value |", "|---|---|",
        ])
        for parameter, value in run.get("config", {}).items():
            if isinstance(value, (list, dict)):
                value = json.dumps(value, ensure_ascii=False)
            lines.append(f"| {markdown_cell(parameter)} | {markdown_cell(value)} |")

        lines.extend([
            "", "### Results", "",
            "| Method | Correct | Accuracy | Difference | Fixed | Broke | Invalid |",
            "|---|---:|---:|---:|---:|---:|---:|",
            f"| Baseline Qwen | {markdown_cell(run.get('qwen_correct'))} | "
            f"{markdown_cell(run.get('qwen_accuracy'))} | N/A | N/A | N/A | "
            f"{markdown_cell(run.get('qwen_invalid_answers'))} |",
        ])

        rag_by_k = run.get("rag_by_k")
        if rag_by_k:
            for k, result in rag_by_k.items():
                lines.append(
                    f"| RAG (k={k}) | {markdown_cell(result.get('correct'))} | "
                    f"{markdown_cell(result.get('accuracy'))} | "
                    f"{markdown_cell(result.get('accuracy_difference'))} | "
                    f"{markdown_cell(result.get('fixed_answers'))} | "
                    f"{markdown_cell(result.get('broke_answers'))} | "
                    f"{markdown_cell(result.get('invalid_answers'))} |"
                )
        elif "rag_correct" in run:  # Support results produced by older versions.
            lines.append(
                f"| RAG (k={run.get('config', {}).get('top_k', 'unknown')}) | "
                f"{markdown_cell(run.get('rag_correct'))} | "
                f"{markdown_cell(run.get('rag_accuracy'))} | "
                f"{markdown_cell(run.get('accuracy_difference'))} | "
                f"{markdown_cell(run.get('rag_fixed_answers'))} | "
                f"{markdown_cell(run.get('rag_broke_answers'))} | N/A |"
            )

        details = run.get("evaluation_details", [])
        if details:
            lines.extend(["", "### Question results", ""])
            for question_number, detail in enumerate(details, start=1):
                expected = detail.get("expected")
                baseline = detail.get("baseline", {})
                lines.extend([
                    f"#### {question_number}. {detail.get('question', 'Question unavailable')}", "",
                    f"- **ID:** {detail.get('question_id', 'unknown')}",
                    f"- **Subject/topic:** {detail.get('subject_name') or 'unknown'} / "
                    f"{detail.get('topic_name') or 'unknown'}",
                    f"- **Gold answer:** {expected}. "
                    f"{detail.get('options', {}).get(expected, 'unavailable')}",
                    f"- **Baseline answer:** {baseline.get('prediction')} "
                    f"({'correct' if baseline.get('is_correct') else 'incorrect'})",
                ])
                for k, rag in detail.get("rag_by_k", {}).items():
                    lines.append(
                        f"- **RAG k={k}:** {rag.get('prediction')} "
                        f"({rag.get('outcome', 'unknown outcome')})"
                    )
                lines.append("")

        lines.extend(["---", ""])

    markdown_path = results_path.with_suffix(".md")
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    return markdown_path

def main(config):
    set_seed(config["seed"])

    textbook_dataset = load_dataset("MedRAG/textbooks")
    corpus = load_textbook_corpus(config["num_documents"], textbook_dataset)

    embedding_model = SentenceTransformer(config["embedding_model"])
    resolved_index_file = embedding_specific_index_file(
        config["index_file"],
        config["embedding_model"],
        config["document_field"],
    )
    index = load_or_build_faiss_index(
        resolved_index_file,
        corpus,
        embedding_model,
        config["embedding_model"],
        config["num_documents"],
        config["document_field"],
    )

    tokenizer, model = load_qwen(config["model_name"])
    resolved_baseline_cache_file = model_specific_cache_file(
        config["baseline_cache_file"],
        config["model_name"],
    )
    model_context_limit = getattr(model.config, "max_position_embeddings", None)
    if (
        isinstance(model_context_limit, int)
        and config["max_input_tokens"] > model_context_limit
    ):
        raise ValueError(
            f"max_input_tokens={config['max_input_tokens']} exceeds the model's "
            f"context limit of {model_context_limit}."
        )

    medmcqa = load_dataset("openlifescienceai/medmcqa")
    evaluation_dataset = load_evaluation_questions(
        config["num_questions"],
        medmcqa,
        config["seed"],
    )

    results = evaluate_qwen_and_rag(
        evaluation_dataset,
        index,
        corpus,
        embedding_model,
        tokenizer,
        model,
        k_values=config["top_k_values"],
        question_only=config["question_only"],
        model_name=config["model_name"],
        max_input_tokens=config["max_input_tokens"],
        baseline_cache_file=resolved_baseline_cache_file,
    )

    run_config = dict(config)
    run_config["resolved_index_file"] = resolved_index_file
    run_config["resolved_baseline_cache_file"] = resolved_baseline_cache_file
    results = {
        "run_time": datetime.now().astimezone().isoformat(),
        "config": run_config,
        **results,
    }

    text_results_file = save_results_to_txt(results, run_config)
    save_results_to_json(results, config["results_file"])
    markdown_results_file = save_results_to_markdown(config["results_file"])

    print(f"Results saved to {config['results_file']}")
    print(f"Text report saved to {text_results_file}")
    print(f"Markdown report saved to {markdown_results_file}")

if __name__ == "__main__":
    arguments = parse_arguments()
    experiment_config = load_config(arguments.config)
    main(experiment_config)
