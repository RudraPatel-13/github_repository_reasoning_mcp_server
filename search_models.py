# search_models.py
from dataclasses import dataclass
from chunk_model import Chunk

@dataclass
class SearchResult:
    chunk: Chunk
    score: float
