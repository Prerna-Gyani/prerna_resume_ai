import streamlit as st
from parser import parse_resume
from ats import ats_score
from enhancer import enhance_openai, enhance_gemini
from utils import generate_docx, generate_pdf

st.set_page_config("AI Resume Builder", layout="wide")

st.title("🤖 AI-Powered Resume Builder & ATS Optimizer")

tab1, tab2 = st.tabs(["Upload Resume", "Manual Entry"])

resume_text = ""

# ---- Upload Resume ----
with tab1:
    file = st.file_uploader("Upload Resume (PDF / DOCX)", type=["pdf","docx"])
    if file:
        resume_text = parse_resume(file)
        st.text_area("Parsed Resume", resume_text, height=300)

# ---- Manual Entry ----
with tab2:
    resume_text = st.text_area(
        "Enter Resume Details",
        height=300,
        placeholder="Education, Skills, Experience..."
    )

# ---- ATS Score ----
if resume_text:
    before_score = ats_score(resume_text)
    st.metric("ATS Score (Before)", before_score)

    col1, col2 = st.columns(2)

    with col1:
        openai_key = st.text_input("OpenAI API Key", type="password")
        if st.button("Enhance with OpenAI"):
            enhanced = enhance_openai(resume_text, openai_key)

    with col2:
        gemini_key = st.text_input("Gemini API Key", type="password")
        if st.button("Enhance with Gemini"):
            enhanced = enhance_gemini(resume_text, gemini_key)

    if "enhanced" in locals():
        st.subheader("✨ Enhanced Resume")
        st.text_area("", enhanced, height=300)

        after_score = ats_score(enhanced)
        st.metric("ATS Score (After)", after_score, delta=after_score-before_score)

        # ---- Download ----
        generate_docx(enhanced, "resume.docx")
        generate_pdf(enhanced, "resume.pdf")

        with open("resume.docx","rb") as f:
            st.download_button("⬇ Download DOCX", f, "resume.docx")

        with open("resume.pdf","rb") as f:
            st.download_button("⬇ Download PDF", f, "resume.pdf")
