# clone_repo.py
import subprocess
from pathlib import Path

def clone_repo(url: str, repo_dir: Path):
    """
    Clone the GitHub repo into repo_dir if it does not already exist.
    Uses shallow clone for speed.
    """
    if repo_dir.exists():
        print(f"[clone_repo] Repo already exists: {repo_dir}")
        return

    print(f"[clone_repo] Cloning into {repo_dir}...")

    subprocess.run(
        ["git", "clone", "--depth", "1", url, str(repo_dir)],
        check=True,
        shell=False
    )

    print("[clone_repo] Clone completed.")
