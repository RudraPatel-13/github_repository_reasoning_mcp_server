# file_reader.py
from pathlib import Path

def read_file_lines(file_path: Path):
    """
    Safely read a text file and return a list of lines.
    Returns [] if file is binary or unreadable.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.readlines()
    except (UnicodeDecodeError, OSError):
        return []
