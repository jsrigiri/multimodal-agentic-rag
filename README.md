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
- LangGraph agent routing system  
- Multi-tool execution (RAG, CSV, Calculator)  
- Vision-based image understanding (Ollama LLaVA)  
- FastAPI serving layer  
- Streamlit UI  
- Docker + CI/CD pipeline  

---

## 🧠 Problem Statement

Build a system that:

- Handles multimodal data (text + structured + images)  
- Dynamically routes queries to the correct tool  
- Provides grounded answers with citations  
- Supports end-to-end ingestion → retrieval → reasoning  
- Runs in a production-ready environment  

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
- Retrieves relevant document chunks
- Supports PDFs, text, and images
- Returns answers with sources

### 📊 CSV Tool
- Data analysis using Pandas
- Supports:
  - Column inspection
  - Row counts
  - Summary statistics
  - Aggregations

### 🧮 Calculator Tool
- Evaluates numeric expressions safely

---

## 🔁 Agent Routing

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
- Ensures system stability and reproducibility  

---

## 🔥 Key Highlights

- Multimodal AI system  
- Agent-based architecture  
- Tool-based reasoning  
- End-to-end pipeline  
- CI/CD + Dockerized deployment  

---

## 📌 Author

Machine Learning + Quant + Agentic AI Portfolio Project
