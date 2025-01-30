# DeepSeek-R1 Local Machine Guide

This repository provides instructions for setting up Ollama with the DeepSeek-R1 model for local LLM interactions. This setup serves as a foundation for Python script integration and n8n workflow automation.

## Overview

Ollama provides local execution of large language models with:

- GPU acceleration support
- Simple CLI interface
- REST API for application integration
- No data sent to third-party services

## Installation

Download and install Ollama from the [official website](https://ollama.ai)

## Using DeepSeek-R1 Natively

To run the DeepSeek-R1 14B model:

1. Run Ollama Server

```bash
ollama serve
```

2. Install and run model

```bash
ollama run deepseek-r1:14b
```

## Using DeepSeek-R1 on Docker

1. Build and start the Ollama server container:

```bash
docker compose up -d
```

2. Wait a few moments for the server to initialize, then pull and run the DeepSeek model:

```bash
docker exec -it ollama-server ollama run deepseek-r1:14b
```

Note: The first run will download the model which may take some time depending on your internet connection.

To stop the container:

```bash
docker compose down
```

The model data is persisted in a Docker volume named `ollama-model-cache` and will be reused on subsequent runs.

## Additional DeepSeek-R1 Models

Browse more models in the [Ollama's DeepSeek Library](https://ollama.com/library/deepseek-r1).

## Integration Examples

- [X] [Python script integration](./python/README.md)
- [ ] N8n workflow automation

## Community & Support

- [Join Ollama Discord](https://discord.gg/ollama)
- [Follow on Twitter](https://twitter.com/ollama_ai)
- [Official Documentation](https://ollama.ai/docs)
