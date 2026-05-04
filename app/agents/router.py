import re
from typing import Literal, TypedDict

from langgraph.graph import END, StateGraph

from app.rag.query_engine import ask_question
from app.tools.csv_tool import answer_csv_question


class AgentState(TypedDict):
    question: str
    route: str
    answer: str
    sources: list


def route_question(state: AgentState) -> AgentState:
    question = state["question"].lower()

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

    if any(k in question for k in calculator_keywords):
        state["route"] = "calculator"
    elif any(k in question for k in csv_keywords):
        state["route"] = "csv"
    else:
        state["route"] = "rag"

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
    result = agent.invoke(
        {
            "question": question,
            "route": "",
            "answer": "",
            "sources": [],
        }
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"],
        "route": result["route"],
    }