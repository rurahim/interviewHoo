from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from parser import parse_jd  # <-- fixed here

app = FastAPI()

@app.get("/")
def root():
    return {"message": "JD Parser running"}

@app.post("/parse-jd")
async def parse_jd_endpoint(file: UploadFile = File(...)):
    content = await file.read()
    parsed = parse_jd(content, file.filename)
    return JSONResponse(content=parsed)

print("Starting JD Parser...")
