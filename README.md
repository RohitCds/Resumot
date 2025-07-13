# 🧠 Resumot: Resume Chat via Local LLM (GGUF Inference)

This project lets you **chat with a pile of PDF resumes** using a **local Large Language Model** running in `.gguf` format via `llama-cpp-python`.  
No API keys. No cloud hosting. Pure local inference. 🔒

---

## 🚀 Features

- 📄 Upload one or more PDF resumes
- 🧠 Chunk and embed resumes using **ChromaDB + Sentence Transformers**
- 🔍 Ask natural language questions like:
  - "Who worked at Google in 2020?"
  - "Which company does John currently work at?"
  - "Who has experience with React?"
- 🤖 Get answers from a **quantized DeepSeek model** running locally (no API needed)

---

## 🏗️ Project Structure
├── main.py # Streamlit UI
├── query_engine.py # GGUF model inference with context injection
├── embedder.py # ChromaDB + SentenceTransformer-based embedding + retrieval
├── resume_parser.py # PDF text extraction and basic chunking
├── sample_resumes/ # Folder for uploaded resumes
├── models/ # Place your GGUF model file here
└── requirements.txt # Dependencies


---

## 📦 Requirements

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```
---

🤖 Model Info
This project uses a quantized DeepSeek Coder 13B (Instruct) model in .gguf format.

📥 Download the model from Hugging Face:

👉 https://huggingface.co/Theros/Q2.5-DeepSeek-R1-DeepThink-test1-Q4_K_M-GGUF

Recommended file: Theros/Q2.5-DeepSeek-R1-DeepThink-test1-Q4_K_M-GGUF

Place it in:
```
~/Desktop/Models/
```
---

🧪 Running the App
```
streamlit run main.py
```
Open your browser to http://localhost:8501 and start chatting with your resumes!

---

💡 How It Works
You upload PDF resumes.

resume_parser.py extracts the raw text.

embedder.py chunks the text and embeds it into a ChromaDB collection using all-mpnet-base-v2.

When you ask a question:

query_engine.py retrieves the most relevant chunks using vector similarity

The question + context is sent to the DeepSeek 13B Instruct model for response generation

The result is streamed back in the UI.

---

📎 Notes
This is the inference-only edition — no fine-tuning or tagging is involved.

If you're on macOS without a GPU, the model still runs thanks to CPU inference using llama.cpp.

Consider reducing context size or switching to a smaller model if your system is resource-constrained.

---

📣 Credits
DeepSeek for the original DeepSeek-Coder model

Theros for the quantized .gguf version: Q2.5-DeepSeek-R1-DeepThink-Q4_K_M

ChromaDB for efficient local vector database

llama-cpp-python for fast local LLM inference in GGUF format

---

🧠 Future Additions
Resume skill/tag extraction via fine-tuning (currently commented in code)

Multi-user interface with persistent resume sessions

CSV export for filtered candidate insights

---

🔓 License
MIT — free to use, fork, and modify. Just give credit if you find this useful!



