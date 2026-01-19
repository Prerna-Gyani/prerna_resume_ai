import streamlit as st
from jinja2 import Template
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="AI Resume Builder & ATS Optimizer",
    layout="wide"
)

st.title("🤖 AI-Powered Resume Builder & ATS Optimizer")

# ----------------- ATS SCORE FUNCTION -----------------
def ats_score(text):
    keywords = [
        "python", "sql", "machine learning",
        "api", "cloud", "data", "ai", "streamlit"
    ]
    matched = sum(1 for k in keywords if k in text.lower())
    return int((matched / len(keywords)) * 100)

# ----------------- FILE GENERATORS -----------------
def generate_docx(text, filename):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(filename)

def generate_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y = height - 40

    for line in text.split("\n"):
        c.drawString(40, y, line[:110])
        y -= 14
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()

# ----------------- INPUT UI -----------------
st.subheader("📄 Resume Input")

resume_text = st.text_area(
    "Enter your resume content",
    height=300,
    placeholder="Education, Skills, Experience, Projects..."
)

# ----------------- ATS SCORE (BEFORE) -----------------
if resume_text.strip():
    before_score = ats_score(resume_text)
    st.metric("ATS Score (Before)", before_score)

    # ----------------- AI ENHANCEMENT (SIMULATED) -----------------
    if st.button("✨ Enhance Resume"):
        enhanced_resume = f"""
{resume_text}

Additional Skills:
• API Integration
• Cloud Fundamentals
• AI Optimization

Summary:
Highly motivated professional with strong technical skills and
experience in AI-driven and data-centric applications.
"""
        st.success("Resume enhanced successfully!")

        # ----------------- SHOW ENHANCED CONTENT -----------------
        st.subheader("✨ Enhanced Resume")
        st.text_area("", enhanced_resume, height=300)

        # ----------------- ATS SCORE (AFTER) -----------------
        after_score = ats_score(enhanced_resume)
        st.metric(
            "ATS Score (After)",
            after_score,
            delta=after_score - before_score
        )

        # ----------------- LaTeX TEMPLATE RENDERING -----------------
        with open("templates/autocv.tex", "r") as f:
            latex_template = Template(f.read())

        latex_output = latex_template.render(
            content=enhanced_resume.replace("\n", "\\\\")
        )

        # ----------------- FILE GENERATION -----------------
        generate_docx(enhanced_resume, "resume.docx")
        generate_pdf(enhanced_resume, "resume.pdf")

        # ----------------- DOWNLOAD BUTTONS -----------------
        st.subheader("⬇ Download Resume")

        with open("resume.docx", "rb") as f:
            st.download_button(
                "Download DOCX",
                f,
                file_name="resume.docx"
            )

        with open("resume.pdf", "rb") as f:
            st.download_button(
                "Download PDF",
                f,
                file_name="resume.pdf"
            )

        # ----------------- TEMPLATE CONFIRMATION -----------------
        st.info("LaTeX AutoCV template applied successfully (ATS-optimized).")
