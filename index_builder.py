# index_builder.py
import json
from pathlib import Path
from embeddings import embed_texts
from index_config import INDEXES_DIR
from index_io import save_vectors, save_chunks

def build_repo_index(repo, chunks):
    repo_id = repo.id
    index_dir = INDEXES_DIR / repo_id
    index_dir.mkdir(parents=True, exist_ok=True)

    print("[index] Embedding chunks (this happens ONCE)...")
    vectors = embed_texts([c.content for c in chunks])

    print("[index] Saving vectors...")
    save_vectors(vectors, index_dir / "vectors.npy")

    print("[index] Saving chunk metadata...")
    save_chunks(chunks, index_dir / "chunks.json")

    meta = {
        "repo_id": repo_id,
        "num_chunks": len(chunks),
        "embedding_model": "all-MiniLM-L6-v2",
    }

    with open(index_dir / "meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    print("[index] Index built successfully")
    return index_dir
