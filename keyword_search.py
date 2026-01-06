# keyword_search.py
import re
from search_models import SearchResult

def keyword_score(text: str, query: str) -> float:
    """
    Simple keyword-based relevance score.
    """
    text = text.lower()
    query = query.lower()

    score = 0.0
    for word in re.findall(r"\w+", query):
        score += text.count(word)

    return score


def search_chunks(chunks, query: str, top_k: int = 5):
    results = []

    for chunk in chunks:
        score = keyword_score(chunk.content, query)
        if score > 0:
            results.append(SearchResult(chunk=chunk, score=score))

    results.sort(key=lambda r: r.score, reverse=True)
    return results[:top_k]
