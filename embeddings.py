# embeddings.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load once (important for performance)
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: list[str]) -> np.ndarray:
    """
    Convert list of texts into embeddings.
    """
    return _model.encode(texts, show_progress_bar=True)

def embed_query(query: str) -> np.ndarray:
    """
    Embed a single query.
    """
    return _model.encode([query])[0]
