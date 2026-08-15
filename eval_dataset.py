# load the evaluation dataset

from datasets import load_dataset

# load MedMCQA from Hugging Face
dataset = load_dataset("openlifescienceai/medmcqa")

# see dataset splits
# we have 182 822 train, 4183 validation and 6150 test questions
# 'id', 'question', 'opa', 'opb', 'opc', 'opd', 'cop', 'choice_type', 'exp', 'subject_name', 'topic_name'
#print(dataset)

# look at the first training example
example = dataset["train"][0]

print("\nFirst training example:")
print(example)

# Print it in a nicer format
print("\nQuestion:")
print(example["question"])

print("\nOptions:")
print("A:", example["opa"])
print("B:", example["opb"])
print("C:", example["opc"])
print("D:", example["opd"])

print("\nCorrect answer:")
print(example["cop"])

for i in range(10):
    example = dataset["train"][i]

    print("\n--------------------")
    print("Question:", example["question"])
    print("A:", example["opa"])
    print("B:", example["opb"])
    print("C:", example["opc"])
    print("D:", example["opd"])
    print("cop:", example["cop"])
    