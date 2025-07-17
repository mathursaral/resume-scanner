import PyPDF2
import docx2txt

def extract_text(file):
    if file.name.endswith(".pdf"):
        pdf = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return str(file.read(), "utf-8")