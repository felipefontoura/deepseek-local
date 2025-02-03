# n8n Workflow Automation with Ollama DeepSeek-R1

This guide explains how to set up and use n8n for workflow automation with Ollama DeepSeek-R1 LLM integration.

## Prerequisites

- Docker and Docker Compose installed
- 16GB RAM minimum (32GB recommended)
- NVIDIA GPU (optional, for acceleration)

## Installation & Setup

1. Start n8n and required services:

```bash
docker compose up -d
```

2. Access n8n:
   - Dashboard URL: <http://localhost:5678>

## Architecture

The n8n setup integrates with several services:

- **Ollama Server**: LLM inference engine (port 11434)
- **Qdrant**: Vector database for embeddings (ports 6333, 6334)
- **n8n**: Workflow automation platform (port 5678)
- **PostgreSQL**: Database for n8n (port 5432)

## Example Workflows

- Simple AI Agent with local Ollaman credentials.
