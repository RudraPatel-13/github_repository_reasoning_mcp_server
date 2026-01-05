# models.py
from dataclasses import dataclass

@dataclass
class RepoFile:
    path: str   # repo-relative POSIX path
    size: int   # size in bytes

@dataclass
class Repo:
    id: str
    root: str   # absolute path to repo root
    files: list[RepoFile]
