from pathlib import Path

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from app.monitoring.metrics import get_metrics

import ollama

from app.ingestion.loaders import load_document
from app.indexing.vector_index import add_text_to_index
from app.rag.query_engine import ask_question
from app.agents.router import run_agent

app = FastAPI(
    title="Multimodal Agentic RAG",
    version="0.1.0",
)

RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Multimodal Agentic RAG API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = RAW_DATA_DIR / file.filename

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    text = load_document(str(file_path))
    add_text_to_index(text=text, source_name=file.filename)

    return {
        "filename": file.filename,
        "saved_path": str(file_path),
        "content_type": file.content_type,
        "status": "uploaded_and_indexed",
    }


@app.post("/ask")
def ask(request: QuestionRequest):
    result = ask_question(request.question)

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"],
    }


@app.post("/agent/ask")
def agent_ask(request: QuestionRequest):
    result = run_agent(request.question)

    return {
        "question": request.question,
        "route": result["route"],
        "answer": result["answer"],
        "sources": result["sources"],
        "latency_ms": result.get("latency_ms"),
        "evaluation": result.get("evaluation"),
    }


@app.get("/ollama/test")
def test_ollama():
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: Ollama is working",
            }
        ],
    )

    return {
        "status": "ok",
        "model": "llama3.2",
        "response": response["message"]["content"],
    }


@app.get("/metrics")
def metrics():
    return get_metrics()