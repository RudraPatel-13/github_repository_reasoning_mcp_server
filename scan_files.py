# scan_files.py
from pathlib import Path
from ignore import should_ignore

def scan_files(repo_root: Path):
    """
    Recursively scan a repository and return all file paths.
    """
    files = []

    for path in repo_root.rglob("*"):
        if path.is_file() and not should_ignore(path):
            files.append(path)

    return files
