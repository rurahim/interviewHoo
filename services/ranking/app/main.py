# interviewhoo/services/ranking/app/main.py

from fastapi import FastAPI, Request
from app.ranker import rank_candidates

app = FastAPI()

@app.post("/rank")
async def rank(request: Request):
    data = await request.json()
    resumes = data.get("resumes", [])
    jd = data.get("job_description", "")
    rankings = rank_candidates(resumes, jd)
    return {"rankings": rankings}
