# 🚀 Multimodal Agentic RAG System (LlamaIndex + LangGraph + FastAPI + Ollama)

![CI](https://github.com/jsrigiri/YOUR_REPO/actions/workflows/ci.yml/badge.svg)
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

This project implements a **production-grade multimodal agentic RAG system** capable of answering questions over:

- PDFs  
- CSV files  
- Text / Markdown  
- Images (via vision models)

It uses an **agent-based architecture** to dynamically route queries to the appropriate tool.

---

## 🏗 Architecture

User Query → Agent Router → Tool Selection:

- RAG Tool (documents + images)
- CSV Tool (Pandas)
- Calculator Tool

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
| CI/CD | GitHub Actions |

---

## 🧪 Testing & CI

```bash
pytest -v
```

CI automatically runs on every push via GitHub Actions.

---

## ▶️ Run the System

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run streamlit_app.py
```

---

## 🔥 Key Highlights

- Multimodal RAG system  
- Agent-based tool routing  
- CI/CD with automated testing  
- End-to-end pipeline  

---

## 📌 Author

Machine Learning + Quant + Agentic AI Portfolio Project
