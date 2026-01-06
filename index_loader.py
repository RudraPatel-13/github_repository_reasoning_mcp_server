# index_loader.py
from index_config import INDEXES_DIR
from index_io import load_vectors, load_chunks

def load_repo_index(repo_id):
    index_dir = INDEXES_DIR / repo_id
    vectors = load_vectors(index_dir / "vectors.npy")
    chunks = load_chunks(index_dir / "chunks.json")
    return chunks, vectors
