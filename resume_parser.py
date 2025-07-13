import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)


# === 🔹 Legacy functions below are unused in the inference-only setup ===
# === 🔹 Retained for compatibility with fine-tuning or extraction-based versions ===


def is_probable_header(line):
    words = line.strip().split()
    if not words:
        return False

    if len(words) <= 5 and line.strip().isupper():
        return True  # ALL CAPS short lines = strong header
    if len(words) <= 4 and line.strip().istitle():
        # Reject lines that match job format
        if "at" in line.lower() and any(char.isdigit() for char in line):
            return False  # Looks like a job, not a header
        return True

    return False


def extract_experience_from_text(text):
    lines = text.split("\n")
    experience_lines = []
    collecting = False

    for line in lines:
        line_lower = line.strip().lower()

        # Look for the Experience section start
        if not collecting and "experience" in line_lower and is_probable_header(line):
            collecting = True
            continue

        # Stop at the next header (whatever it is)
        if collecting and is_probable_header(line):
            break

        if collecting:
            experience_lines.append(line)

    return "\n".join(experience_lines).strip()
