import re
import os
import time
from typing import Literal, TypedDict

from langgraph.graph import END, StateGraph

from app.rag.query_engine import ask_question
from app.tools.csv_tool import answer_csv_question
from app.monitoring.metrics import record_request
from app.evaluation.rag_eval import evaluate_rag
from app.config import LLM_MODEL_NAME, USE_LLM_ROUTER

import ollama


class AgentState(TypedDict):
    question: str
    route: str
    answer: str
    sources: list


def keyword_route_question(question: str) -> str:
    q = question.lower()

    calculator_keywords = [
        "calculate",
        "compute",
        "sum",
        "percentage",
        "ratio",
    ]

    csv_keywords = [
        "csv",
        "column",
        "row",
        "dataframe",
        "table",
        "average",
        "mean",
        "statistics",
        "summary",
    ]

    if any(k in q for k in calculator_keywords):
        return "calculator"

    if any(k in q for k in csv_keywords):
        return "csv"

    return "rag"


def llm_route_question(question: str) -> str:
    if not USE_LLM_ROUTER:
        return keyword_route_question(question)

    prompt = f"""
You are a routing classifier for an agentic RAG system.

Choose exactly one route:

- rag: for questions about uploaded PDFs, text files, markdown files, images, documents, or general document understanding
- csv: for questions about CSV files, tables, columns, rows, dataframe summaries, statistics, or averages
- calculator: for direct math expressions or calculations

Question:
{question}

Return only one word: rag, csv, or calculator.
"""

    try:
        response = ollama.chat(
            model=LLM_MODEL_NAME
            messages=[{"role": "user", "content": prompt}],
        )

        route = response["message"]["content"].strip().lower()

        if "calculator" in route:
            return "calculator"
        if "csv" in route:
            return "csv"
        if "rag" in route:
            return "rag"

    except Exception:
        pass

    return keyword_route_question(question)


def route_question(state: AgentState) -> AgentState:
    state["route"] = llm_route_question(state["question"])
    return state


def calculator_tool(state: AgentState) -> AgentState:
    question = state["question"]

    expression = re.sub(
        r"[^0-9\.\+\-\*\/\(\)\s]",
        "",
        question,
    ).strip()

    if not expression:
        state["answer"] = (
            "Calculator tool selected, but I could not find a numeric expression to calculate."
        )
        state["sources"] = []
        return state

    try:
        result = eval(expression, {"__builtins__": {}})
        state["answer"] = f"The calculation result is: {result}"
    except Exception as e:
        state["answer"] = f"Calculator error: {e}"

    state["sources"] = []
    return state


def rag_tool(state: AgentState) -> AgentState:
    result = ask_question(state["question"])
    state["answer"] = result["answer"]
    state["sources"] = result["sources"]
    return state


def csv_tool(state: AgentState) -> AgentState:
    result = answer_csv_question(state["question"])
    state["answer"] = result["answer"]
    state["sources"] = result["sources"]
    return state


def choose_route(state: AgentState) -> Literal["calculator", "csv", "rag"]:
    return state["route"]


def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("router", route_question)
    graph.add_node("calculator", calculator_tool)
    graph.add_node("rag", rag_tool)
    graph.add_node("csv", csv_tool)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
    "router",
    choose_route,
    {
        "calculator": "calculator",
        "csv": "csv",
        "rag": "rag",
    },
)

    graph.add_edge("calculator", END)
    graph.add_edge("rag", END)
    graph.add_edge("csv", END)

    return graph.compile()


agent = build_agent()


def run_agent(question: str):
    start = time.time()

    result = agent.invoke(
        {
            "question": question,
            "route": "",
            "answer": "",
            "sources": [],
        }
    )

    latency_ms = (time.time() - start) * 1000

    record_request(result["route"], latency_ms)

    eval_metrics = evaluate_rag(
        question,
        result["answer"],
        result["sources"],
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"],
        "route": result["route"],
        "latency_ms": round(latency_ms, 2),
        "evaluation": eval_metrics,
    }