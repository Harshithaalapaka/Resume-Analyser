import pdfplumber
from docx import Document
import io

def extract_text(file_data : bytes, file_name :str)-> str:
    if file_name.lower().endswith('.pdf'):
        return _extract_pdf(file_data)
    elif file_name.lower().endswith('.docx'):
        return _extract_docx(file_data)
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")

def _extract_pdf(file_data:bytes) -> str:
    text=[]
    with pdfplumber.open(io.BytesIO(filebytes)) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def _extract_docx(file_bytes:bytes)->str:
    doc= Document(io.BytesIO(file_bytes))
    text=[]
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)
