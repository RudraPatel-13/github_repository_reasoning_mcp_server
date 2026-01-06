# vector_search.py
from embeddings import embed_texts, embed_query
from similarity import cosine_similarity

def build_index(chunks):
    texts = [c.content for c in chunks]
    vectors = embed_texts(texts)
    return vectors

def semantic_search(chunks, vectors, query: str, top_k: int = 5):
    query_vec = embed_query(query)

    scores = []
    for i, vec in enumerate(vectors):
        score = cosine_similarity(query_vec, vec)
        scores.append((score, chunks[i]))

    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_k]
