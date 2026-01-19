from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_docx(text, path):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(path)

def generate_pdf(text, path):
    c = canvas.Canvas(path, pagesize=A4)
    y = 800
    for line in text.split("\n"):
        c.drawString(40, y, line[:100])
        y -= 15
        if y < 40:
            c.showPage()
            y = 800
    c.save()
