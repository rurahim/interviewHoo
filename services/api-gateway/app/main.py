from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/parse-resume")
async def parse_resume(request: Request):
    async with httpx.AsyncClient() as client:
        body = await request.body()
        headers = dict(request.headers)
        headers.pop("host", None)
        resp = await client.post(
            "http://resume-parser:8001/parse",  # uses container name and correct port
            content=body,
            headers=headers
        )
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers=dict(resp.headers),
            media_type=resp.headers.get("content-type")
        )
    
@app.post("/parse-jd")
async def parse_jd(request: Request):
    # Forward the request to the JD Parser microservice
    async with httpx.AsyncClient() as client:
        body = await request.body()
        headers = dict(request.headers)
        headers.pop("host", None)
        resp = await client.post(
            "http://jd-parser:8000/parse-jd",  # correct endpoint
            content=body,
            headers=headers
        )
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers=dict(resp.headers),
            media_type=resp.headers.get("content-type")
        )

print("✅ API Gateway running")
