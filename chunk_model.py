# chunk_model.py
from dataclasses import dataclass

@dataclass
class Chunk:
    id: str              # unique chunk id
    file_path: str       # repo-relative POSIX path
    language: str        # python, js, markdown, etc.
    start_line: int
    end_line: int
    content: str
