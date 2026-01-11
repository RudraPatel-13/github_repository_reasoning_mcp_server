# github_repository_reasoning_mcp_server
# MCP GitHub Repository Reasoning Engine

A semantic search and reasoning system that allows an AI to answer
questions about any GitHub repository using **Retrieval-Augmented Generation (RAG)**.

---

## What This Project Does

Given:
- a GitHub repository URL
- a natural language question

This system:
1. Loads and chunks the repository
2. Converts chunks into semantic embeddings
3. Builds a persistent vector index
4. Performs semantic search over the index
5. Returns the most relevant code/documentation chunks
6. Allows an LLM (ChatGPT / Claude) to answer accurately using real repo data

---

## Architecture Overview

