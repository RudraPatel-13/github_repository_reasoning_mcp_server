from load_repo import load_repo
from chunk_repo import chunk_repo
from index_builder import build_repo_index
from index_loader import load_repo_index
from indexed_search import search_index

def ask_repo(github_url: str, question: str, top_k: int = 5):
    repo = load_repo(github_url)
    repo_id = repo.id

    try:
        load_repo_index(repo_id)
    except FileNotFoundError:
        chunks = chunk_repo(repo)
        build_repo_index(repo, chunks)

    results = search_index(repo_id, question, top_k)

    return [
        {
            "file_path": c["file_path"],
            "start_line": c["start_line"],
            "end_line": c["end_line"],
            "score": score,
        }
        for score, c in results
    ]
