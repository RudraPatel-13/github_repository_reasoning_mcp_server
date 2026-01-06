# language_detector.py

EXTENSION_LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".jsx": "javascript",
    ".java": "java",
    ".go": "go",
    ".rs": "rust",
    ".cpp": "cpp",
    ".c": "c",
    ".md": "markdown",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
}

def detect_language(file_path: str) -> str:
    file_path = file_path.lower()

    for ext, language in EXTENSION_LANGUAGE_MAP.items():
        if file_path.endswith(ext):
            return language

    return "text"
