from fastapi import FastAPI
from pydantic import BaseModel
from mcp_tools import ask_repo

app = FastAPI(title="GitHub Repo Reasoning API")

class Query(BaseModel):
    github_url: str
    question: str
    top_k: int = 5

@app.post("/ask")
def ask(query: Query):
    return ask_repo(
        github_url=query.github_url,
        question=query.question,
        top_k=query.top_k
    )
