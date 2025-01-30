# Python Ollama Integration

A Python application for interacting with Ollama's local LLM services.

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running on your machine
- pip (Python package installer)

## Installation

1. Clone the repository

```bash
git clone https://github.com/felipefontoura/deepseek-local.git
cd deepseek-local/python
```

2. Create and activate virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Run Ollama Server:

```bash
ollama server
```

2. Run the main application:

```bash
python main.py
```

## Troubleshooting

Common issues and solutions:

- Ensure Ollama is running before starting the application
- Check if all required dependencies are installed
- Verify Python version compatibility
