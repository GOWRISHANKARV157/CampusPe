# AI API Integration Examples

This repository contains examples for integrating with various AI/LLM APIs, including Cohere, Gemini, Groq, Hugging Face, and Ollama.

## Project Structure

- `cohere_example.py` - Example integration with Cohere API
- `gemini_example.py` - Example integration with Google Gemini API
- `groq_example.py` - Example integration with Groq API
- `huggingface_example.py` - Example integration with Hugging Face Inference API
- `ollama_example.py` - Example integration with Ollama (local LLM service)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your API keys:
```
COHERE_API_KEY=your_cohere_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
OLLAMA_API_KEY=your_ollama_api_key_here (optional, for local Ollama)
```

## Usage

Run any individual example script:

```bash
python cohere_example.py
python gemini_example.py
python groq_example.py
python huggingface_example.py
python ollama_example.py
```

Each script will prompt you to enter a prompt/query and display the API response.

## API Details

### Cohere
- **Model**: command-xlarge-nightly
- **Max Tokens**: 200
- **Temperature**: 0.7
- [Cohere Documentation](https://docs.cohere.com/)

### Gemini
- **Model**: gemini-2.5-flash
- [Gemini Documentation](https://ai.google.dev/)

### Groq
- **Model**: llama-3.1-8b-instant
- **Max Tokens**: 200
- **Temperature**: 0.7
- [Groq Documentation](https://console.groq.com/docs/)

### Hugging Face
- **Model**: meta-llama/Meta-Llama-3-8B-Instruct
- **Max Tokens**: 200
- [Hugging Face Documentation](https://huggingface.co/docs/inference-client/)

### Ollama
- **Model**: llama3
- **Endpoint**: http://localhost:11434/api/generate
- **Note**: Requires Ollama to be running locally
- [Ollama Documentation](https://ollama.com/)

## Requirements

See `requirements.txt` for all Python package dependencies.

## Notes

- All examples use environment variables for API key management
- Each script includes error handling for failed API requests
- Prompts are limited to 200 tokens for most APIs
- Ollama is a local service and doesn't require an API key by default

## License

This project is for educational purposes.
