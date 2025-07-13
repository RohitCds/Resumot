import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Set up ChromaDB client
chroma_client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = chroma_client.get_or_create_collection(name="resumes")

# Load the sentence transformer model
embedding_model = SentenceTransformer("all-mpnet-base-v2")

def embed_resume_chunks(chunks, candidate_name):
    # Encode all chunks
    embeddings = embedding_model.encode(chunks).tolist()
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[f"{candidate_name}_{i}"],
            metadatas=[{"candidate": candidate_name}]
        )
    print(f"✅ Embedded {len(chunks)} chunks for {candidate_name}")

def query_resume_collection(query, top_k=10):
    query_embedding = embedding_model.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results