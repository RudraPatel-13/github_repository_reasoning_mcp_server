# index_io.py
import json
import numpy as np
from pathlib import Path

def save_vectors(vectors, path: Path):
    np.save(path, vectors)

def load_vectors(path: Path):
    return np.load(path)

def save_chunks(chunks, path: Path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "file_path": c.file_path,
                    "start_line": c.start_line,
                    "end_line": c.end_line,
                    "language": c.language,
                }
                for c in chunks
            ],
            f,
            indent=2
        )

def load_chunks(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
