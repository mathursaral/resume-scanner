# resume-scanner
Resume Scanner with spaCy + Streamlit

Attempt to build a Resume Scanner with spaCy + Streamlit that:

Uploads a resume (PDF/DOCX/text),
Highlights missing keywords based on a specific job role,
Uses spaCy for keyword/NER analysis,
Uses Streamlit for a quick web UI.

pip install -r requirements.txt
python -m spacy download en_core_web_sm

streamlit run app.py

App will run on port 8501

