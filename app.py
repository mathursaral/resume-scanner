# app.py

import streamlit as st
import spacy
from keyword_library import job_keywords
from parser import extract_text

st.set_page_config(page_title="Resume Scanner", layout="centered")

nlp = spacy.load("en_core_web_sm")

st.title("📄 Resume Scanner with spaCy + Streamlit")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

job_role = st.selectbox("Choose the target job role", list(job_keywords.keys()))

if uploaded_file and job_role:
    resume_text = extract_text(uploaded_file).lower()
    resume_doc = nlp(resume_text)

    with st.expander("📜 Extracted Resume Text"):
        st.write(resume_text)

    required_keywords = job_keywords[job_role]
    found = [kw for kw in required_keywords if kw in resume_text]
    missing = list(set(required_keywords) - set(found))

    st.subheader("✅ Keywords Found")
    st.write(", ".join(found) if found else "No keywords found.")

    st.subheader("❌ Keywords Missing")
    st.write(", ".join(missing) if missing else "None! You're all set! 🚀")
