from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import faiss


DATASET_NAME = "MedRAG/textbooks"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
 # NUM_DOCUMENTS = 10_000 # small chunk


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


def retrieve_documents(query, index, corpus, embedding_model, k=5):
    query_embedding = embedding_model.encode(
        [query],
        normalize_embeddings=True
    )
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


if __name__ == "__main__":
    # Load textbook corpus
    print("Loading textbook corpus...")

    dataset = load_dataset(DATASET_NAME)
    corpus = dataset["train"]

    NUM_DOCUMENTS = len(corpus) # all textbooks

    small_corpus = corpus.select(range(min(NUM_DOCUMENTS, len(corpus))))

    print(f"Using {len(small_corpus)} chunks.")

    # Load embedding model
    print("\nLoading embedding model...")

    embedding_model = SentenceTransformer(EMBEDDING_MODEL)

    index = build_faiss_index(small_corpus, embedding_model)

    # Test retrieval
    queries = [
        (
            "Chronic urethral obstruction due to benign prismatic hyperplasia can lead to the following change in kidney parenchyma\n"
            "A. Hyperplasia\nB. Hyperophy\nC. Atrophy\nD. Dyplasia"
        ),
        (
            "Which vitamin is supplied from only animal source?\n"
            "A. Vitamin C\nB. Vitamin B7\nC. Vitamin B12\nD. Vitamin D"
        ),
        (
            "All of the following are surgical options for morbid obesity except\n"
            "A. Adjustable gastric banding\nB. Biliopancreatic diversion\n"
            "C. Duodenal Switch\nD. Roux en Y Duodenal By pass"
        ),
        (
            "Following endaerectomy on the right common carotid, a patient is found to be blind in the right eye. "
            "It appears that a small thrombus embolized during surgery and lodged in the artery supplying the optic nerve. "
            "Which artery would be blocked?\n"
            "A. Central artery of the retina\nB. Infraorbital artery\n"
            "C. Lacrimal artery\nD. Nasociliary artery"
        ),
        (
            "Growth hormone has its effect on growth through?\n"
            "A. Directly\nB. IG1-1\nC. Thyroxine\nD. Intranuclear receptors"
        ),
        (
            "Scrub typhus is transmitted by: September 2004\n"
            "A. Louse\nB. Tick\nC. Mite\nD. Milk"
        ),
        (
            "Abnormal vascular patterns seen with colposcopy in case of cervical intraepithelial neoplasia are all except\n"
            "A. Punctation\nB. Mosaicism\nC. Satellite lesions\nD. Atypical vessels"
        ),
        (
            "Per rectum examination is not a useful test for diagnosis of\n"
            "A. Anal fissure\nB. Hemorrhoid\nC. Pilonidal sinus\nD. Rectal ulcer"
        ),
        (
            "Characteristics of Remifentanyl: a) Metabolised by plasma esterase, b) Short half life, "
            "c) More potent than Alfentanyl, d) Dose reduced in hepatic and renal disease, "
            "e) Duration of action more than Alfentanyl\n"
            "A. ab\nB. bc\nC. abc\nD. bcd"
        ),
        (
            "Hypomimia is?\n"
            "A. Decreased ability to copy\nB. Decreased execution\n"
            "C. Deficit of expression by gesture\nD. Deficit of fluent speech"
        ),
    ]

    # Print retrieved chunks
    for query_number, query in enumerate(queries, start=1):
        retrieved_documents = retrieve_documents(
            query,
            index,
            small_corpus,
            embedding_model,
            k=5,
        )

        print("\n" + "#" * 80)
        print(f"Query {query_number}:")
        print(query)

        print("\nTop retrieved chunks:")

        for rank, result in enumerate(retrieved_documents, start=1):
            example = result["document"]

            print("\n" + "=" * 80)
            print(f"Rank: {rank}")
            print(f"Similarity: {result['similarity']:.3f}")
            print(f"Title: {example['title']}")
            print(f"ID: {example['id']}")
            print()
            print(example["content"])
