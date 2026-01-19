def ats_score(resume_text, job_keywords=None):
    keywords = job_keywords or [
        "python","machine learning","api","sql",
        "data","cloud","ai","streamlit"
    ]
    matched = sum(1 for k in keywords if k.lower() in resume_text.lower())
    score = int((matched / len(keywords)) * 100)
    return min(score, 95)
