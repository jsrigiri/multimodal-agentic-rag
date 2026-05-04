from llama_index.core import Settings

from app.indexing.vector_index import load_existing_index


Settings.llm = None


def ask_question(question: str):
    index = load_existing_index()

    if index is None:
        return {
            "answer": "No documents have been indexed yet. Please upload a PDF, CSV, TXT, Markdown, or image file first.",
            "sources": [],
        }

    retriever = index.as_retriever(similarity_top_k=3)
    retrieved_nodes = retriever.retrieve(question)

    sources = []
    context_parts = []

    for node_with_score in retrieved_nodes:
        node = node_with_score.node
        text = node.get_content()

        context_parts.append(text)

        sources.append(
            {
                "source": node.metadata.get("source", "unknown"),
                "text": text[:300],
                "score": float(node_with_score.score or 0.0),
            }
        )

    if not context_parts:
        return {
            "answer": "I could not find relevant information in the indexed documents.",
            "sources": [],
        }

    answer = "\n\n".join(context_parts[:2])

    return {
        "answer": answer,
        "sources": sources,
    }