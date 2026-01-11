from index_loader import load_repo_index
from embeddings import embed_query
from similarity import cosine_similarity

def search_index(repo_id: str, query: str, top_k: int = 5):
    chunks, vectors = load_repo_index(repo_id)
    query_vec = embed_query(query)

    scored = []
    for i, vec in enumerate(vectors):
        score = cosine_similarity(query_vec, vec)
        scored.append((score, chunks[i]))

    scored.sort(key=lambda x: x[0], reverse=True)

    seen = set()
    results = []
    for score, chunk in scored:
        key = (chunk["file_path"], chunk["start_line"], chunk["end_line"])
        if key in seen:
            continue
        seen.add(key)
        results.append((score, chunk))
        if len(results) >= top_k:
            break

    return results
