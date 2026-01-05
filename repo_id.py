# repo_id.py
import re

def make_repo_id(owner: str, repo: str) -> str:
    
    safe_repo = re.sub(r"[^a-zA-Z0-9_-]", "_", repo)
    safe_owner = re.sub(r"[^a-zA-Z0-9_-]", "_", owner)

    return f"{safe_owner}_{safe_repo}"
