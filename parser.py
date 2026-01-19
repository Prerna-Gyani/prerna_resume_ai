import fitz
from docx import Document

def parse_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

def parse_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def parse_resume(file):
    if file.name.endswith(".pdf"):
        return parse_pdf(file)
    return parse_docx(file)
