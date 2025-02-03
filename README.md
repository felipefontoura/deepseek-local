# Ollama DeepSeek-R1 Local Machine Guide

This repository provides instructions for setting up Ollama with the DeepSeek-R1 model for local LLM interactions. This setup serves as a foundation for Python script integration and n8n workflow automation.

## Overview

Ollama enables local execution of large language models with:

- GPU acceleration support
- Simple CLI interface
- REST API for application integration
- No data transmission to third-party services

## Installation

Download and install Ollama from the [official website](https://ollama.ai)

## Using Ollama DeepSeek-R1 Natively

To run the DeepSeek-R1 model:

1. Start the Ollama Server:

```bash
ollama serve
```

2. Install and run the model:

```bash
ollama run deepseek-r1:7b
```

## Using Ollama DeepSeek-R1 with Docker

The setup includes several services working together:

- **Ollama Server**: LLM inference engine (port 11434)
- **OpenWeb UI**: Web interface for Ollama (port 3000)
- **n8n**: Workflow automation platform (port 5678)
- **Qdrant**: Vector database for embeddings (ports 6333, 6334)
- **PostgreSQL**: Database for n8n (port 5432)

### Starting the Services

1. Start all containers:

```bash
docker compose up -d
```

The DeepSeek-R1 7B model will be automatically downloaded and loaded when the container starts.

2. Access the services:
   - OpenWeb UI: <http://localhost:3000>
   - n8n Dashboard: <http://localhost:5678>
   - Qdrant Dashboard: <http://localhost:6333/dashboard>

To stop the containers:

```bash
docker compose down
```

Data persistence:

- Model data: `ollama-model-cache` volume
- n8n data: `n8n-data` volume
- OpenWeb UI data: `open-webui-data` volume
- PostgreSQL data: `postgres-data` volume
- Qdrant data: `qdrant-data` volume

### GPU Support (Optional)

To enable GPU support:

1. Uncomment the GPU-related sections in `docker-compose.yml`
2. Change OpenWeb UI image to `ghcr.io/open-webui/open-webui:cuda`

## Additional DeepSeek-R1 Models

Browse additional models in the [Ollama DeepSeek Library](https://ollama.com/library/deepseek-r1).

## Integration Examples

- [X] [Python script integration](./python/README.md)
- [x] [n8n workflow automation](./n8n/README.md)

## Community & Support

- [Join Ollama Discord](https://discord.gg/ollama)
- [Follow on Twitter](https://twitter.com/ollama_ai)
- [Official Documentation](https://ollama.ai/docs)
