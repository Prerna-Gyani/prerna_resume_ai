# prerna_resume_ai

---

# AI-Powered Resume Builder & ATS Optimization Agent

## Overview

The AI-Powered Resume Builder & ATS Optimization Agent is a Streamlit-based web application designed to help job seekers create **professionally formatted, ATS-optimized resumes** with minimal manual effort.
The system evaluates resume content, enhances it using AI, applies an ATS-friendly LaTeX template, and generates ready-to-submit documents in **PDF and DOCX formats**.

---

## Problem Statement

Many resumes are rejected by Applicant Tracking Systems due to poor keyword alignment, inconsistent formatting, or unclear descriptions. Manually optimizing resumes for ATS systems is time-consuming and error-prone.

This project automates resume enhancement and formatting while maintaining professional standards and ATS compatibility.

---

## Key Features

* Resume input via manual entry or file upload (PDF/DOCX)
* Automated ATS score calculation
* AI-driven content enhancement for clarity and keyword optimization
* Professional LaTeX (AutoCV-style) resume formatting
* Resume generation in PDF and DOCX formats
* ATS score comparison before and after enhancement
* Modular and scalable architecture
* Streamlit Cloud deployment support

---

## System Architecture

The application is structured into independent, reusable modules:

* User interface and workflow orchestration via Streamlit
* Resume parsing and text extraction
* ATS score evaluation
* AI-based resume enhancement
* Template-based formatting
* File generation and download handling

This modular design ensures clarity, maintainability, and scalability.

---

## Application Workflow

1. User uploads an existing resume or enters details manually.
2. Resume text is parsed and structured.
3. An initial ATS score is calculated.
4. AI enhances resume content to improve tone, clarity, and keyword density.
5. Enhanced content is mapped into a LaTeX AutoCV-style template.
6. Final resumes are generated in PDF and DOCX formats.
7. Updated ATS score is displayed for comparison.

---

## Sample Output – Example 1 (Manual Resume Input)

### User Input

Personal Information
Name: Rahul Sharma
Education: B.Tech in Computer Science
Skills: Python, SQL, Data Analysis
Experience: Data Analyst Intern
Projects: Resume Parser Tool

### ATS Score (Before Enhancement)

Score: 61 / 100
Identified gaps include missing keywords such as API integration, cloud concepts, and AI optimization.

### AI-Enhanced Resume Output

Professional Summary
Detail-oriented Data Analyst with strong expertise in Python, SQL, and data analysis. Experienced in building AI-driven applications, optimizing resumes for ATS systems, and developing scalable data solutions.

Enhanced Skills Section
Python, SQL, Data Analysis, Machine Learning Fundamentals, API Integration, Cloud Basics, AI Optimization Techniques

Experience Enhancement

* Designed and deployed data-driven applications with improved ATS keyword alignment
* Assisted in developing AI-based resume parsing and optimization tools

### ATS Score (After Enhancement)

Score: 88 / 100
Improvement: +27 points

### Generated Files

* Professional Resume (PDF)
* Editable Resume (DOCX)

---

## Sample Output – Example 2 (Uploaded Resume)

### Input

Uploaded PDF resume with unstructured formatting and limited keyword usage.

### ATS Score (Before Enhancement)

Score: 54 / 100

### AI Enhancement Summary

* Improved grammar and sentence structure
* Added role-specific keywords aligned with job descriptions
* Reorganized content for ATS readability

### ATS Score (After Enhancement)

Score: 84 / 100
Improvement: +30 points

### Output

* ATS-optimized resume in PDF format
* Editable DOCX resume with professional formatting

---

## Technologies Used

* Python
* Streamlit
* OpenAI API
* Google Gemini API
* LaTeX (AutoCV-style template)
* ReportLab
* python-docx
* Jinja2

---

## Deployment

* Platform: Streamlit Cloud
* Entry Point: app.py
* Secure API key handling via environment variables

---

## Use Cases

* Job seekers optimizing resumes for ATS systems
* Students and fresh graduates preparing professional resumes
* Academic AI agent projects
* Resume optimization demonstrations

---

## Conclusion

This project demonstrates the practical application of AI in resume optimization by combining ATS analysis, content enhancement, and professional formatting into a single automated workflow. The system delivers measurable improvements in ATS scores while maintaining high presentation standards.

---

## Project Summary

An AI-powered resume optimization platform that evaluates, enhances, and generates ATS-friendly resumes with professional LaTeX formatting.

---

## System Architecture 1: High-Level System Architecture
```
flowchart LR
    U[User] -->|Resume Upload / Manual Entry| UI[Streamlit Web UI]
    UI --> ATS[ATS Scoring Engine]
    UI --> AI[AI Enhancement Engine]
    AI --> TPL[LaTeX Template Engine]
    TPL --> GEN[Resume Generator]
    GEN --> OUT[PDF & DOCX Output]
    OUT --> U
```
* User interacts through a Streamlit web interface
* Resume content is scored for ATS compatibility
* AI enhances the resume content
* LaTeX templates ensure professional formatting
* Final resumes are generated and downloaded

---

## 🖥️ SAMPLE OUTPUT – AI-Powered Resume Builder & ATS Optimizer

---

## 🤖 AI-Powered Resume Builder & ATS Optimizer

### Tabs at the top:

```
[ Upload Resume ]   [ Manual Entry ]
```

---

## 🔹 Case 1: Manual Entry (Sample)

### 📝 Manual Resume Input

```
Name: ABC Gyani
Email: abc.gyani@gmail.com
Phone: +91-98XXXXXX21

Education:
B.Tech in Computer Science, JNTU Hyderabad (2021)

Skills:
Python, SQL, Machine Learning, Data Analysis, Streamlit

Experience:
Data Analyst Intern at ABC Tech
- Built data dashboards using Streamlit
- Worked on ML models for prediction

Projects:
AI Resume Parser using Python
```

---

## 📊 ATS SCORE (Before Enhancement)

```
ATS Score (Before): 62 / 100
```

📉 *Missing keywords: cloud, api, ai optimization*

---

## 🔐 API Input Section

```
OpenAI API Key:  ********************
Gemini API Key:  ********************
```

Buttons:

```
[ Enhance with OpenAI ]   [ Enhance with Gemini ]
```

---

## ✨ AI-ENHANCED RESUME (Sample Output)

```
ABC Gyani
Data Analyst | AI & ML Enthusiast

Professional Summary:
Detail-oriented Data Analyst with strong expertise in Python,
SQL, Machine Learning, and AI-driven application development.
Experienced in building ATS-optimized resumes, data dashboards,
and scalable analytics solutions.

Education:
Bachelor of Technology in Computer Science
Jawaharlal Nehru Technological University, Hyderabad – 2021

Technical Skills:
• Python, SQL, Streamlit
• Machine Learning & Data Analysis
• API Integration & Cloud Fundamentals
• AI Optimization Techniques

Professional Experience:
Data Analyst Intern – ABC Tech
• Designed and deployed interactive Streamlit dashboards
• Implemented machine learning models to improve prediction accuracy
• Optimized data pipelines and API integrations

Projects:
AI-Powered Resume Parser
• Built an AI-driven resume parsing and optimization tool using Python
• Improved ATS matching score by integrating keyword analysis
```

---

## 📈 ATS SCORE (After Enhancement)

```
ATS Score (After): 88 / 100
⬆ Improvement: +26 points
```

🟢 *Keywords optimized: python, ai, api, cloud, machine learning*

---

## 📥 DOWNLOAD OPTIONS

```
⬇ Download DOCX
⬇ Download PDF
```

✔ **resume.docx** (Editable)
✔ **resume.pdf** (Submission-ready)

---

## 🧾 FILES GENERATED (Backend)

```
resume.docx
resume.pdf
```

---

## 🏁 Final Outcome

| Feature               | Status |
| --------------------- | ------ |
| Resume Parsing        | ✅      |
| ATS Scoring           | ✅      |
| AI Enhancement        | ✅      |
| Template Formatting   | ✅      |
| DOCX Export           | ✅      |
| PDF Export            | ✅      |
| Streamlit Cloud Ready | ✅      |

---

