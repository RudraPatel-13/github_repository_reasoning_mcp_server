# parse_url.py
from urllib.parse import urlparse

def parse_github_url(url: str):
    parsed = urlparse(url)

    if parsed.netloc.lower() != "github.com":
        raise ValueError("Not a GitHub URL")

    parts = parsed.path.strip("/").split("/")
    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    owner = parts[0]
    repo = parts[1]

    if repo.endswith(".git"):
        repo = repo[:-4]

    return owner, repo
