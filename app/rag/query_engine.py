from llama_index.core import Settings

from app.indexing.vector_index import load_existing_index


Settings.llm = None


def ask_question(question: str):
    index = load_existing_index()

    if index is None:
        return {
            "answer": "No documents have been indexed yet. Please upload a PDF, CSV, TXT, or Markdown file first.",
            "sources": [],
        }

    query_engine = index.as_query_engine(
        similarity_top_k=3,
        response_mode="compact",
    )

    response = query_engine.query(question)

    sources = []
    if hasattr(response, "source_nodes"):
        for node in response.source_nodes:
            sources.append({
                "source": node.metadata.get("source", "unknown"),
                "text": node.text[:300],
            })

    return {
        "answer": str(response),
        "sources": sources,
    }