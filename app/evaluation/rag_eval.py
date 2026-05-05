def evaluate_rag(question: str, answer: str, sources: list):
    has_sources = len(sources) > 0

    # simple keyword overlap
    q_words = set(question.lower().split())
    a_words = set(answer.lower().split())

    overlap = len(q_words & a_words)
    relevance_score = overlap / len(q_words) if q_words else 0

    return {
        "has_sources": has_sources,
        "answer_length": len(answer),
        "relevance_score": round(relevance_score, 2),
    }