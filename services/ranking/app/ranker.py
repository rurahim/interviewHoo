# interviewhoo/services/ranking/app/ranker.py

from typing import List, Dict
import difflib

def rank_candidates(resumes: List[str], jd: str) -> List[Dict]:
    ranked = []
    for idx, resume in enumerate(resumes):
        score = difflib.SequenceMatcher(None, resume.lower(), jd.lower()).ratio()
        ranked.append({
            "candidate_id": idx + 1,
            "score": round(score * 100, 2)
        })
    # Sort by score descending
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked
