# config.py
from pathlib import Path

WORKSPACE = Path.home() / "mcp" / "workspace"
REPOS_DIR = WORKSPACE / "repos"

REPOS_DIR.mkdir(parents=True, exist_ok=True)
