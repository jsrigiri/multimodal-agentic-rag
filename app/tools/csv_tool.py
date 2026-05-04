from pathlib import Path

import pandas as pd


RAW_DATA_DIR = Path("data/raw")


def get_latest_csv_path():
    csv_files = sorted(
        RAW_DATA_DIR.glob("*.csv"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    if not csv_files:
        return None

    return csv_files[0]


def answer_csv_question(question: str):
    csv_path = get_latest_csv_path()

    if csv_path is None:
        return {
            "answer": "No CSV file found. Please upload a CSV first.",
            "sources": [],
        }

    df = pd.read_csv(csv_path)
    q = question.lower()

    if "columns" in q:
        answer = f"Columns in {csv_path.name}: {list(df.columns)}"

    elif "rows" in q or "row count" in q:
        answer = f"{csv_path.name} has {len(df)} rows."

    elif "summary" in q or "statistics" in q or "describe" in q:
        answer = df.describe(include="all").to_string()

    elif "average" in q or "mean" in q:
        numeric_cols = df.select_dtypes(include="number").columns.tolist()

        matched_col = None
        for col in numeric_cols:
            if col.lower() in q:
                matched_col = col
                break

        if matched_col:
            value = df[matched_col].mean()
            answer = f"The average of {matched_col} in {csv_path.name} is {value:.4f}."
        else:
            answer = f"Numeric columns available for average: {numeric_cols}"

    else:
        answer = (
            "CSV tool selected. I can answer questions about columns, row count, "
            "summary statistics, and averages for numeric columns."
        )

    return {
        "answer": answer,
        "sources": [{"source": csv_path.name, "text": "CSV analyzed with Pandas"}],
    }