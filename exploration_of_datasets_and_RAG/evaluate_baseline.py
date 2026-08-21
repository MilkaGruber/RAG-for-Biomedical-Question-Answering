import torch
import random
import numpy as np
import re

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM

# take care of reproducabillity 
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

torch.use_deterministic_algorithms(True)
torch.backends.cudnn.benchmark = False

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
NUM_QUESTIONS = 100


# --------------------------------------------------
# 1. Load Qwen
# --------------------------------------------------
print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto",
)
model.eval()
print("Model loaded.")


# --------------------------------------------------
# 2. Load MedMCQA
# --------------------------------------------------
print("Loading dataset...")
dataset = load_dataset("openlifescienceai/medmcqa")
evaluation_dataset = dataset["validation"].select(
    range(NUM_QUESTIONS)
)
print(f"Loaded {len(evaluation_dataset)} questions.")


# --------------------------------------------------
# 3. Function for asking Qwen a MCQ
# --------------------------------------------------
def ask_model(question, option_a, option_b, option_c, option_d):
    prompt = f"""
        Question:
        {question}

        A. {option_a}
        B. {option_b}
        C. {option_c}
        D. {option_d}

        Answer with only one letter: A, B, C, or D.
        """

    messages = [
        {
            "role": "system",
            "content": "You are a medical question answering assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    model_inputs = tokenizer(
        text,
        return_tensors="pt"
    ).to(model.device)

    with torch.inference_mode():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=5,
            do_sample=False,
        )

    # Remove input tokens
    generated_ids = generated_ids[
        :, model_inputs.input_ids.shape[1]:
    ]

    answer = tokenizer.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return answer.strip()


# --------------------------------------------------
# 4. Convert MedMCQA's numeric answer to A/B/C/D
# --------------------------------------------------
def convert_correct_answer(cop):
    mapping = {0: "A", 1: "B", 2: "C", 3: "D"}
    return mapping[cop]


def extract_answer_letter(answer):
    """Extract an isolated A, B, C, or D from the model response."""
    match = re.search(r"\b[A-D]\b", answer.upper())
    return match.group(0) if match else None


# --------------------------------------------------
# 5. Evaluate
# --------------------------------------------------
correct = 0
for i, example in enumerate(evaluation_dataset):

    prediction = ask_model(
        example["question"],
        example["opa"],
        example["opb"],
        example["opc"],
        example["opd"],
    )

    correct_answer = convert_correct_answer(example["cop"])
    prediction_letter = extract_answer_letter(prediction)

    print(
        f"{i:03d}: raw={prediction!r}, "
        f"predicted={prediction_letter!r}, expected={correct_answer!r}"
    )

    if prediction_letter == correct_answer:
        correct += 1


# --------------------------------------------------
# 6. Calculate accuracy
# --------------------------------------------------
accuracy = correct / len(evaluation_dataset)

print("\n----------------------------")
print("RESULTS")
print("----------------------------")
print(f"Questions: {len(evaluation_dataset)}")
print(f"Correct:   {correct}")
print(f"Incorrect: {len(evaluation_dataset) - correct}")
print(f"Accuracy:  {accuracy:.2%}") # we got 45%
