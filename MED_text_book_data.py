from datasets import load_dataset

DATASET_NAME = "MedRAG/textbooks"
NUM_DOCUMENTS = 10_000


print("Loading textbook corpus...")
dataset = load_dataset(DATASET_NAME)

print("\nDataset structure:")
print(dataset)


# Inspect available split names
print("\nAvailable splits:")
print(dataset.keys())


# Most Hugging Face datasets use a 'train' split for corpus-style data.
# Take the first available split.
split_name = list(dataset.keys())[0]
corpus = dataset[split_name]


print(f"\nUsing split: {split_name}")
print(f"Total number of chunks: {len(corpus)}")


# Inspect one raw example
print("\nFirst raw example:")
print(corpus[0])
# we get 'id', 'title', 'content', 'contents'


# Take only a small subset for now
num_documents = min(NUM_DOCUMENTS, len(corpus))

small_corpus = corpus.select(range(num_documents))


print(f"\nUsing {len(small_corpus)} chunks for the first experiment.")


# Print a few examples
print("\nExample chunks:")
print("-" * 80)

for i in range(5):
    print(f"\nCHUNK {i}")
    print(small_corpus[i])
    print("-" * 80)