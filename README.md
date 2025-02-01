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

1. Start containers:

```bash
docker compose up -d
```

The DeepSeek-R1 7B model will be automatically downloaded and loaded when the container starts.

2. Access the OpenWeb UI at <http://localhost:3000>

To stop the containers:

```bash
docker compose down
```

Model data is persisted in a Docker volume named `ollama-model-cache` and will be reused on subsequent runs.

## Additional DeepSeek-R1 Models

Browse additional models in the [Ollama DeepSeek Library](https://ollama.com/library/deepseek-r1).

## Integration Examples

- [X] [Python script integration](./python/README.md)
- [ ] n8n workflow automation

## Community & Support

- [Join Ollama Discord](https://discord.gg/ollama)
- [Follow on Twitter](https://twitter.com/ollama_ai)
- [Official Documentation](https://ollama.ai/docs)
