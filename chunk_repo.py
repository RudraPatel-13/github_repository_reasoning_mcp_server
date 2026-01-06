# chunk_repo.py
from pathlib import Path
from chunk_file import chunk_file

# Skip noisy / non-useful directories
SKIP_PREFIXES = (
    "test/",
    "tests/",
    "__tests__/",
    ".github/",
)

def chunk_repo(repo):
    """
    Chunk all files in a repository.
    Returns a flat list of Chunk objects.
    """
    all_chunks = []
    repo_root = Path(repo.root)

    for i, repo_file in enumerate(repo.files):
        # Progress logging
        if i % 200 == 0:
            print(f"[chunk_repo] Processing file {i}/{len(repo.files)}")

        # Skip test and CI files
        if repo_file.path.startswith(SKIP_PREFIXES):
            continue

        file_path = repo_root / repo_file.path
        chunks = chunk_file(file_path, repo_root)
        all_chunks.extend(chunks)

    return all_chunks
