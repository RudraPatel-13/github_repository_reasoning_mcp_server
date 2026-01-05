# load_repo.py

from config import REPOS_DIR
from parse_url import parse_github_url
from repo_id import make_repo_id
from clone_repo import clone_repo
from scan_files import scan_files
from normalize_path import normalize_path
from models import Repo, RepoFile


def load_repo(url: str) -> Repo:
    """
    Load a GitHub repository into the local workspace and
    return structured metadata about it.
    """
    # 1. Parse URL
    owner, repo = parse_github_url(url)

    # 2. Generate stable repo ID
    repo_id = make_repo_id(owner, repo)

    # 3. Determine local repo directory
    repo_dir = REPOS_DIR / repo_id

    # 4. Clone if needed
    clone_repo(url, repo_dir)

    # 5. Scan & filter files
    paths = scan_files(repo_dir)

    # 6. Build RepoFile objects
    repo_files = [
        RepoFile(
            path=normalize_path(path, repo_dir),
            size=path.stat().st_size
        )
        for path in paths
    ]

    # 7. Return Repo object
    return Repo(
        id=repo_id,
        root=str(repo_dir),
        files=repo_files
    )
