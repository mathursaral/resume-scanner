# app.py

import streamlit as st
from keyword_library import job_keywords
from parser import extract_text
from analyzer import check_sections, analyze_format, keyword_match_score, readability_score

st.set_page_config(page_title="ATS Resume Checker", layout="centered")

st.title("📋 ATS Resume Checker")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])
job_role = st.selectbox("Select Job Role", list(job_keywords.keys()))

if uploaded_file and job_role:
    resume_text = extract_text(uploaded_file).lower()
    
    st.subheader("📄 Resume Analysis Report")

    with st.expander("🔍 Extracted Text"):
        st.text(resume_text[:2000] + ("..." if len(resume_text) > 2000 else ""))

    # Section Check
    found_sec, missing_sec = check_sections(resume_text)
    st.markdown(f"**✅ Sections Found:** {', '.join(found_sec) or 'None'}")
    st.markdown(f"**❌ Sections Missing:** {', '.join(missing_sec) or 'None'}")

    # Formatting
    format_issues = analyze_format(uploaded_file.name, resume_text)
    if format_issues:
        st.warning("⚠️ Formatting Issues:")
        for issue in format_issues:
            st.write("- " + issue)
    else:
        st.success("✅ Format looks good!")

    # Keyword Score
    score, found_kw, missing_kw = keyword_match_score(resume_text, job_keywords[job_role])
    st.markdown(f"**🧠 Keyword Match Score:** {score}/100")
    st.progress(score)
    st.write("✅ Found Keywords: ", ", ".join(found_kw) or "None")
    st.write("❌ Missing Keywords: ", ", ".join(missing_kw) or "None")

    # Readability
    avg_len = readability_score(resume_text)
    st.write(f"📝 **Average Sentence Length**: {avg_len} words/sentence")
    if avg_len > 25:
        st.warning("⚠️ Sentences may be too long. Consider breaking them down.")
    elif avg_len < 10:
        st.info("ℹ️ Sentences are short. That’s good for readability!")

    # Final verdict
    if score >= 80 and not missing_sec and not format_issues:
        st.success("🎯 Your resume is highly optimized for ATS!")
    else:
        st.info("🔧 Consider improving the above areas to make your resume ATS-friendly.")
