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

This project implements a **production-grade multimodal agentic RAG platform** capable of answering questions over:

- PDFs  
- CSV files  
- Text / Markdown  
- Images (vision-enabled)

The system combines **retrieval, reasoning, and tool-based execution** using an agent architecture similar to modern enterprise AI systems.

---

## 🧠 Why This Project Matters (Interview Gold)

This project demonstrates:

- Real-world **agentic AI system design**
- **Multimodal reasoning** (text + structured + vision)
- **Production-grade ML engineering**
- **End-to-end pipeline ownership**
- **CI/CD + Docker deployment**

You can confidently say:

> “I built a multimodal agentic RAG system with dynamic tool routing, vector retrieval, and production-ready deployment.”

---

## 🏗 Architecture

```text
User Query
   ↓
LangGraph Agent Router
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
Answer + Sources
```

---

## 🧩 Architecture Diagram (Conceptual)

```text
[User]
   ↓
[FastAPI Layer]
   ↓
[Agent Router (LangGraph)]
   ↓
 ┌──────────────┬──────────────┬──────────────┐
 |   RAG Tool   |   CSV Tool   | Calculator   |
 └──────────────┴──────────────┴──────────────┘
   ↓
[Vector Store + Embeddings]
   ↓
[LLM / Vision Model]
   ↓
[Response + Sources]
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
| Testing | Pytest |
| DevOps | Docker, GitHub Actions |

---

## 🧠 Agent Tools

### 🔍 RAG Tool
- Retrieves document chunks
- Supports PDF, text, and image-derived text
- Returns grounded answers with citations

### 📊 CSV Tool
- Data analysis via Pandas
- Supports:
  - Columns
  - Row counts
  - Summary stats
  - Aggregations

### 🧮 Calculator Tool
- Safe expression evaluation
- Handles numeric queries

---

## 🔁 Query Routing

```text
User Question → Router → Tool

Examples:
- "What is this document about?" → RAG
- "What are the columns?" → CSV Tool
- "Calculate 1250 * 0.08" → Calculator
```

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
- Ensures reliability and reproducibility  

---

## 📸 UI Preview (Add Screenshot)

Add screenshot here after running Streamlit:

```text
streamlit run streamlit_app.py
```

---

## 🔥 Key Highlights

- Multimodal AI system  
- Agent-based architecture  
- Tool-based reasoning  
- Real-time API + UI  
- CI/CD + Dockerized deployment  
- End-to-end ML system design  

---

## 🚀 Future Improvements

- LLM-based intelligent routing  
- Multi-step reasoning agents  
- Hybrid retrieval (BM25 + vector)  
- Observability & monitoring  
- Cloud deployment (AWS / GCP)  

---

## 📌 Author

Machine Learning + Quant + Agentic AI Portfolio Project
