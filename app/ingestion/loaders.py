from pathlib import Path

import fitz
import pandas as pd
from PIL import Image
import ollama


def load_pdf(file_path: str) -> str:
    text_parts = []

    with fitz.open(file_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            text_parts.append(f"\n--- Page {page_num} ---\n{text}")

    return "\n".join(text_parts)


def load_csv(file_path: str) -> str:
    df = pd.read_csv(file_path)

    preview = df.head(20).to_markdown(index=False)
    summary = df.describe(include="all").to_string()

    return f"""
CSV file: {Path(file_path).name}

Preview:
{preview}

Summary:
{summary}
"""


def load_text(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8", errors="ignore")


def load_document(file_path: str) -> str:
    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return load_pdf(file_path)

    if suffix == ".csv":
        return load_csv(file_path)

    if suffix in [".txt", ".md"]:
        return load_text(file_path)

    if suffix in [".png", ".jpg", ".jpeg"]:
        return load_image(file_path)

    raise ValueError(f"Unsupported file type: {suffix}")


def load_image(file_path: str) -> str:
    response = ollama.chat(
        model="llava:7b",
        messages=[
            {
                "role": "user",
                "content": (
                    "Describe this image in detail. "
                    "If it contains a chart, table, screenshot, or document, "
                    "summarize the key visible information."
                ),
                "images": [file_path],
            }
        ],
    )

    caption = response["message"]["content"]

    return f"""
Image file: {Path(file_path).name}

Vision summary:
{caption}
"""