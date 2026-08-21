import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"

def ask_model(question):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME) # loads tokenizer

    model = AutoModelForCausalLM.from_pretrained( # loads model
        MODEL_NAME,
        torch_dtype="auto",
        device_map="auto",
    )

    messages = [
        {
            "role": "system",
            "content": "You are a helpful medical question answering assistant."
        },
        {
            "role": "user",
            "content": question
        }
    ]

    # convert to format for Qwen
    text = tokenizer.apply_chat_template( 
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

# Convert text into token IDs
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    # Generate an answer
    with torch.no_grad():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=100,
            do_sample=False,
        )


    # remove the input tokens
    generated_ids = generated_ids[:, model_inputs.input_ids.shape[1]:]


    # convert to text
    answer = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return answer

if __name__ == "__main__":
    answer1 = ask_model("What is melanoma? Answer in two sentences.")
    answer2 = ask_model("What is melanoma? Answer in a longer paragraph.")

    print("\nMODEL ANSWERS:")
    print(answer1)
    print(answer2)


