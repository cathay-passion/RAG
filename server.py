from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from team import initv2m
import uvicorn

app = FastAPI()

# 設定 CORS（可按需求調整 allow_origins）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

v2m_team = initv2m()

@app.get("/")
async def read_root():
    return {"message": "Hello, AGNO!"}

@app.post("/query")
async def get_response(query: Query):
    response_text = ""
    for response in v2m_team.ask(query.question):
        response_text += response
    return response_text.strip()

if __name__ == "__main__":
    uvicorn.run(
        "server:app",       # 如果檔名不是 main.py，請改成 "你的檔名:app"
        host="localhost",
        port=9999,
        reload=True       # ← 加這行就會自動重啟
    )
