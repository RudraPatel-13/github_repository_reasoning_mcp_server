# ignore.py

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "target",
    ".venv",
    "__pycache__",
}

IGNORE_EXTS = {
    ".lock",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".zip",
    ".exe",
    ".dll",
    ".pdf",
}

def should_ignore(path):
    # Ignore directories anywhere in path
    for part in path.parts:
        if part.lower() in IGNORE_DIRS:
            return True

    # Ignore file extensions
    if path.suffix.lower() in IGNORE_EXTS:
        return True

    return False
