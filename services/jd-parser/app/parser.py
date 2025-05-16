import pdfplumber
import io

def parse_jd(file_bytes: bytes, filename: str) -> dict:
    """
    Extracts text from a Job Description (JD) PDF using pdfplumber.
    Returns basic mock structure for now.
    """
    raw_text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                raw_text += page.extract_text() or ""
    except Exception as e:
        raw_text = f"Error extracting text: {e}"
    
    return {
        "title": "Software Engineer",  # mock
        "skills": ["Python", "FastAPI", "Docker"],  # mock
        "raw_text": raw_text[:500]  # limit output
    }
