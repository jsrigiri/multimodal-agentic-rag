from app.agents.router import run_agent


def test_calculator_route():
    result = run_agent("Calculate 1250 * 0.08")

    assert result["route"] == "calculator"
    assert "100" in result["answer"]


def test_csv_route_without_csv_does_not_crash():
    result = run_agent("What are the columns in the CSV?")

    assert result["route"] == "csv"
    assert "answer" in result
    assert "sources" in result


def test_rag_route_without_index_does_not_crash():
    result = run_agent("What is this document about?")

    assert result["route"] == "rag"
    assert "answer" in result
    assert "sources" in result