from sentence_transformers import SentenceTransformer
import torch



# Load embedding model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Melanoma is a malignant tumor arising from melanocytes.",
    "Metoprolol is a beta-1 selective adrenergic blocker.",
    "The kidneys filter blood and produce urine.",
    "Insulin lowers blood glucose by promoting glucose uptake.",
    "Aspirin inhibits cyclooxygenase and reduces platelet aggregation."
]

# embed the documents 
document_embeddings = embedding_model.encode(documents, convert_to_tensor=True)

print("Document embedding shape:")
print(document_embeddings.shape)

query = "What type of drug is metoprolol?"


query_embedding = embedding_model.encode(query, convert_to_tensor=True)

# compute the similarities to query
similarities = torch.nn.functional.cosine_similarity(
    query_embedding.unsqueeze(0),
    document_embeddings
)

sorted_indices = torch.argsort(similarities, descending=True)


print("\nQuery:")
print(query)

print("\nSearch results:")

for index in sorted_indices:
    index = index.item()
    print(
        f"{similarities[index]:.3f} | "
        f"{documents[index]}"
    )