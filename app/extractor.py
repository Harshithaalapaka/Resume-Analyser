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
