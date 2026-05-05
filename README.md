# 🚀 Multimodal Agentic RAG Platform (LlamaIndex + LangGraph + FastAPI + Ollama)

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![RAG](https://img.shields.io/badge/RAG-LlamaIndex-orange)
![Agents](https://img.shields.io/badge/Agents-LangGraph-red)
![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-yellow)
![API](https://img.shields.io/badge/API-FastAPI-green)
![UI](https://img.shields.io/badge/UI-Streamlit-purple)
![Vision](https://img.shields.io/badge/Vision-Ollama%20LLaVA-blue)
![Testing](https://img.shields.io/badge/Testing-Pytest-lightgrey)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

---

## 📌 Overview

This project implements a **production-grade multimodal agentic RAG platform** combining:

- Document ingestion (PDF, CSV, TXT, Images)  
- LlamaIndex-based retrieval pipeline  
- LangGraph agent routing system (LLM + fallback)  
- Multi-tool execution (RAG, CSV, Calculator)  
- Vision-based image understanding (Ollama LLaVA)  
- FastAPI serving layer  
- Streamlit UI  
- Docker + CI/CD  
- Observability + evaluation metrics  

---

## 🧠 Problem Statement

Build a system that:

- Handles multimodal data (text + structured + images)  
- Dynamically routes queries using intelligent agents  
- Provides grounded answers with citations  
- Tracks performance (latency, usage, quality)  
- Runs as a production-ready service  

---

## 🏗 Architecture

```text
User Query
   ↓
LangGraph Agent Router (LLM + fallback)
   ↓
Tool Selection
   ├── RAG Tool (LlamaIndex)
   ├── CSV Tool (Pandas)
   ├── Calculator Tool
   ↓
Vector Retrieval (ChromaDB)
   ↓
Vision Processing (Ollama LLaVA)
   ↓
Answer + Sources + Metrics
```

---

## ⚙️ Tech Stack

| Layer | Tools |
|------|------|
| API | FastAPI |
| UI | Streamlit |
| Agent | LangGraph |
| RAG | LlamaIndex |
| Vector DB | ChromaDB |
| Data Tool | Pandas |
| Vision | Ollama (LLaVA) |
| Monitoring | Custom metrics |
| Evaluation | RAG scoring |
| Testing | Pytest |
| DevOps | Docker, GitHub Actions |

---

## 🧠 Agent Tools

### 🔍 RAG Tool
- Retrieves relevant document chunks  
- Supports PDFs, text, and images  
- Returns grounded answers with citations  

### 📊 CSV Tool
- Data analysis using Pandas  
- Supports columns, row counts, statistics, averages  

### 🧮 Calculator Tool
- Safe numeric expression evaluation  

---

## 🔁 Intelligent Routing

- Keyword-based fallback routing  
- LLM-based routing using Ollama (optional)  

---

## 📊 Observability

Tracks:
- Total requests  
- Tool usage distribution  
- Average latency  

Endpoint:

```bash
GET /metrics
```

---

## 🧪 Evaluation (RAG Quality)

Each response includes:
- `has_sources`
- `answer_length`
- `relevance_score`

---

## 🧪 Testing

```bash
pytest -v
```

Includes:
- API tests  
- Agent routing tests  
- Integration test (upload → index → ask)  

---

## ▶️ Run System

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run streamlit_app.py
```

---

## 🐳 Docker

```bash
docker-compose up --build
```

---

## 🔁 CI/CD

- GitHub Actions runs tests on every push  
- Ensures stability and reproducibility  

---

## ⚠️ Deployment Note (Render Memory Requirement)

This project includes a `render.yaml` configuration for deployment.

However:

- **Render free tier (512MB RAM) is NOT sufficient**
- The system uses memory-intensive components:
  - LlamaIndex  
  - ChromaDB  
  - Sentence Transformers  
  - Multimodal processing  

These require **≥1GB RAM (recommended 2GB)**.

### Recommended Deployment Options

- Render (paid instance ≥1GB RAM)  
- Railway / Fly.io  
- AWS EC2 / ECS  

### Best Option for Demo

```bash
docker-compose up --build
```

---

## 🔥 Key Highlights

- Multimodal AI system  
- Agent-based architecture  
- LLM + rule-based routing  
- Observability + evaluation  
- End-to-end pipeline  
- CI/CD + Docker deployment  
- Deployment-aware design  

---

## 📌 Author

Machine Learning + Quant + Agentic AI Portfolio Project
