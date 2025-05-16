from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .parser import parse_resume

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/parse")
def parse(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    file_bytes = file.file.read()
    parsed_data = parse_resume(file_bytes, file.filename)
    return JSONResponse(content=parsed_data)

print("✅ Resume Parser running")
