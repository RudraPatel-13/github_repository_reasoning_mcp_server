# chunk_file.py
from pathlib import Path
from chunk_model import Chunk
from language_detector import detect_language
from file_reader import read_file_lines

MAX_FILE_SIZE = 500_000     # 500 KB
MAX_CHUNKS_PER_FILE = 20

MAX_LINES = 200
MIN_LINES = 20
OVERLAP = 20

def chunk_file(file_path: Path, repo_root: Path):
    """
    Split a single file into overlapping line-based chunks.
    """
    lines = read_file_lines(file_path)

    # Skip very large files
    if file_path.stat().st_size > MAX_FILE_SIZE:
        return []
    
    # Skip small or unreadable files
    if len(lines) < MIN_LINES:
        return []

    chunks = []
    language = detect_language(file_path.as_posix())

    start = 0
    chunk_index = 0

    while start < len(lines):
        end = min(start + MAX_LINES, len(lines))
        chunk_lines = lines[start:end]

        if len(chunk_lines) < MIN_LINES:
            break

        content = "".join(chunk_lines)

        chunk_id = f"{file_path.name}:{chunk_index}"

        chunks.append(
            Chunk(
                id=chunk_id,
                file_path=file_path.relative_to(repo_root).as_posix(),
                language=language,
                start_line=start + 1,
                end_line=end,
                content=content,
            )
        )

        if len(chunks) >= MAX_CHUNKS_PER_FILE:
            break


        # Move forward with overlap
        start = end - OVERLAP
        chunk_index += 1

    return chunks
