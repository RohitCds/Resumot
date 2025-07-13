import os
import streamlit as st
from resume_parser import extract_text_from_pdf, chunk_text
from embedder import embed_resume_chunks
from query_engine import ask_resume_agent

# === Streamlit UI Setup ===
st.set_page_config(page_title="🧠 Resumot", layout="centered", initial_sidebar_state="collapsed")
st.title("📄 Resumot: Chat with Your Resume Pile")

st.markdown("""
Upload resumes (PDF), ask questions like:
- "Who has experience in NLP?"
- "What tools does Monday use?"
- "Who worked at Amazon in 2020?"
""")

# === Upload Section ===
UPLOAD_DIR = "sample_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"Uploaded {len(uploaded_files)} files.")
    for file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        # Extract and embed resume
        text = extract_text_from_pdf(file_path)
        chunks = chunk_text(text)
        candidate_name = os.path.splitext(file.name)[0]
        embed_resume_chunks(chunks, candidate_name)

    st.success("✅ All resumes parsed and embedded!")

# === Query Section ===
st.markdown("### Ask a question about the resumes:")
user_query = st.text_input("Ask anything:")

if user_query:
    with st.spinner("Thinking..."):
        answer, context_used = ask_resume_agent(user_query)
        st.markdown("### 🤖 Answer:")
        st.markdown(answer)

        # Optional: Show retrieved chunks (transparency)
        with st.expander("🔍 Resume Context Used"):
            st.code(context_used)
