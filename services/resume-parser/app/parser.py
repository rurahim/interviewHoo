import pdfplumber
import io

def parse_resume(file_bytes: bytes, filename: str) -> dict:
    raw_text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                raw_text += page.extract_text() or ""
    except Exception as e:
        raw_text = f"Error extracting text: {e}"
    raw_text = raw_text[:500]
    return {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "raw_text": raw_text
    }
