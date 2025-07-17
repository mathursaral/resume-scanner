# analyzer.py

import re
import spacy

nlp = spacy.load("en_core_web_sm")

REQUIRED_SECTIONS = ['summary', 'experience', 'education', 'skills']

def check_sections(text):
    found = []
    for section in REQUIRED_SECTIONS:
        if re.search(rf"\b{section}\b", text.lower()):
            found.append(section)
    missing = list(set(REQUIRED_SECTIONS) - set(found))
    return found, missing

def analyze_format(file_name, text):
    issues = []
    if not file_name.endswith(".pdf"):
        issues.append("Resume is not in PDF format.")
    if len(text.split()) < 200:
        issues.append("Resume is too short. Consider adding more content.")
    if len(text.split()) > 1200:
        issues.append("Resume is too long. Consider shortening.")
    return issues

def keyword_match_score(text, keyword_list):
    found = [kw for kw in keyword_list if kw in text]
    score = int((len(found) / len(keyword_list)) * 100)
    return score, found, list(set(keyword_list) - set(found))

def readability_score(text):
    doc = nlp(text)
    avg_sent_len = sum(len(sent) for sent in doc.sents) / len(list(doc.sents))
    return round(avg_sent_len, 2)
