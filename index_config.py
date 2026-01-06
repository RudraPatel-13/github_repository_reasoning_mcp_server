# index_config.py
from pathlib import Path

WORKSPACE = Path.home() / "mcp" / "workspace"
INDEXES_DIR = WORKSPACE / "indexes"

INDEXES_DIR.mkdir(parents=True, exist_ok=True)
