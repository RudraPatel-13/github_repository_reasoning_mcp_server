# normalize_path.py
from pathlib import Path

def normalize_path(path: Path, repo_root: Path) -> str:
    """
    Convert absolute Windows path into repo-relative POSIX path.
    """
    return path.relative_to(repo_root).as_posix()
