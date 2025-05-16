# Resume Parser Microservice

This microservice extracts text from PDF resumes and returns basic information in JSON format. It is built with FastAPI and uses `pdfplumber` for PDF text extraction.

## Features
- Accepts PDF files via a `/parse` POST endpoint
- Extracts and returns the first 500 characters of text from the PDF
- Returns mock name and email fields (for demonstration)

## API Endpoints
- `GET /` — Health check
- `POST /parse` — Accepts a PDF file upload and returns parsed data

## Running Locally

### Prerequisites
- Python 3.11+ (other versions may work, but 3.11 is used in Docker)
- `pip` (Python package manager)

### Install dependencies
```bash
pip install -r requirements.txt
```

### Start the service
From the `interviewhoo/services/resume-parser` directory, run:
```bash
uvicorn app.main:app --reload --port 8001
```

The service will be available at [http://localhost:8001](http://localhost:8001).

### Example Usage
Send a POST request to `/parse` with a PDF file:
```bash
curl -X POST "http://localhost:8001/parse" -F "file=@your_resume.pdf"
```

## Docker
You can also run the service using Docker:
```bash
docker build -t resume-parser .
docker run -p 8001:8001 resume-parser
```

---

This service is intended as a starting point for more advanced resume parsing and extraction.
