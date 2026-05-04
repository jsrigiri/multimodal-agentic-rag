# 🚀 Multimodal Agentic RAG System (LlamaIndex + LangGraph + FastAPI + Ollama)

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![RAG](https://img.shields.io/badge/RAG-LlamaIndex-orange)
![Agents](https://img.shields.io/badge/Agents-LangGraph-red)
![API](https://img.shields.io/badge/API-FastAPI-green)
![UI](https://img.shields.io/badge/UI-Streamlit-purple)
![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-yellow)
![Vision](https://img.shields.io/badge/Vision-Ollama%20LLaVA-blue)
![Testing](https://img.shields.io/badge/Testing-Pytest-lightgrey)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

---

## 📌 Overview

This project implements a **production-grade multimodal agentic RAG (Retrieval-Augmented Generation) system** capable of answering questions over:

- PDFs  
- CSV files  
- Text / Markdown  
- Images (via vision models)

It combines **retrieval, reasoning, and tool-based decision-making** using an agent architecture.

---

## 🧠 Problem Statement

Build a system that:

- Supports multimodal data (text + images + structured data)  
- Dynamically routes queries to the correct tool  
- Provides grounded answers with citations  
- Enables real-time interaction via API and UI  
- Mimics modern enterprise AI assistant systems  

---

## 🏗 Architecture

```text
User Query
   ↓
LangGraph Agent Router
   ↓
Tool Selection:
   - RAG Tool (Documents + Images)
   - CSV Tool (Pandas)
   - Calculator Tool
   ↓
LlamaIndex Retrieval
   ↓
ChromaDB Vector Store
   ↓
Ollama Vision Model (Images)
   ↓
Final Answer + Sources
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

---

## 🧠 Agent Tools

### 🔍 RAG Tool
- Retrieves relevant chunks from documents
- Supports PDFs, text, and images
- Returns answers with sources

### 📊 CSV Tool
- Uses Pandas for analysis
- Supports:
  - Column inspection
  - Row counts
  - Summary statistics
  - Averages

### 🧮 Calculator Tool
- Parses and evaluates numeric expressions
- Safe execution environment

---

## 🖼 Multimodal Capability

- Image ingestion and indexing  
- Vision-based summarization using LLaVA  
- Images become searchable context  

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
- Agent routing tests  
- API tests  

---

## ▶️ Run the System

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start API

```bash
uvicorn app.main:app --reload
```

### 3. Start UI

```bash
streamlit run streamlit_app.py
```

---

## 🔥 Key Highlights

- Multimodal RAG system  
- Agent-based tool routing  
- Local vision model integration  
- Structured answers with citations  
- End-to-end pipeline (ingestion → retrieval → reasoning → serving)  

---

## 📌 Future Improvements

- LLM-based intelligent routing  
- Multi-step reasoning agents  
- Hybrid retrieval (BM25 + vector)  
- Monitoring & observability  
- Docker + cloud deployment  

---

## 📌 Author

Machine Learning + Quant + Agentic AI Portfolio Project
