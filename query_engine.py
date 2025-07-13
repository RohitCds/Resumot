from embedder import query_resume_collection
from llama_cpp import Llama
import os

MODEL_PATH = os.path.expanduser("~/Desktop/Models/Q2.5-DeepSeek-R1-DeepThink-Q4_K_M.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6,
    n_gpu_layers=0
)

def fetch_relevant_chunks(query):
    result = query_resume_collection(query)
    docs = result.get("documents", [[]])[0]
    return "\n".join(docs) if docs else "No data found."

def ask_resume_agent(query):
    context = fetch_relevant_chunks(query)
    prompt = (
        "You are an assistant who analyzes resumes and answers questions based on them. Use ONLY the provided text below.\n\n"
        f"{context}\n\n"
        f"Question: {query}\nAnswer:"
    )
    resp = llm(prompt, max_tokens=300, temperature=0.3, stop=["\nQuestion:", "</s>"])
    return resp["choices"][0]["text"].strip(), context