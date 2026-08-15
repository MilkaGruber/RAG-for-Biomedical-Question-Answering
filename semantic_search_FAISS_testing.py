from sentence_transformers import SentenceTransformer
import faiss

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
document_embeddings = embedding_model.encode(documents, normalize_embeddings=True)

print("Document embedding shape:")
print(document_embeddings.shape)

# create FAISS index
embedding_dimension = document_embeddings.shape[1]
index = faiss.IndexFlatIP(embedding_dimension)

index.add(document_embeddings)
print("Number of vectors in FAISS:")
print(index.ntotal)

# embed query
query = "What type of drug is metoprolol?"
query_embedding = embedding_model.encode([query],normalize_embeddings=True)

# search FAISS
k = 3
similarities, indices = index.search(query_embedding, k)

# print results 
print("\nQuery:")
print(query)
print("\nSearch results:")

for similarity, index_id in zip(
    similarities[0],
    indices[0]
):
    print(
        f"{similarity:.3f} | "
        f"{documents[index_id]}"
    )