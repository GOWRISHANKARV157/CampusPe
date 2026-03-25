# Setup Guide - AI API Integration

This guide walks you through setting up the AI API integration project step-by-step.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [API Key Configuration](#api-key-configuration)
4. [Testing the Setup](#testing-the-setup)
5. [Troubleshooting](#troubleshooting)

---

## System Requirements

- **Python**: 3.8 or higher
- **pip**: Latest version
- **OS**: Windows, macOS, or Linux
- **Internet Connection**: Required for API calls (except Ollama which runs locally)

### Check Your Python Installation

Open your terminal/command prompt and run:

```bash
python --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

---

## Installation Steps

### Step 1: Navigate to Project Directory

```bash
cd "path/to/assignment 3"
```

### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- cohere
- google-generativeai
- groq
- huggingface-hub
- requests
- python-dotenv

---

## API Key Configuration

### Step 1: Create `.env` File

In the project root directory, create a new file named `.env` (note: no extension):

**On Windows (Command Prompt):**
```bash
type nul > .env
```

**On macOS/Linux or Windows (PowerShell):**
```bash
New-Item -Path ".env" -ItemType File
```

Or simply create it manually in your text editor.

### Step 2: Add Your API Keys

Edit the `.env` file and add your API keys in the following format:

```
COHERE_API_KEY=your_cohere_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
OLLAMA_API_KEY=your_ollama_api_key_here
```

### How to Get Each API Key

#### **Cohere API Key**
1. Visit [cohere.com](https://cohere.com)
2. Sign up for a free account
3. Go to Dashboard → API Keys
4. Copy your API key and add it to `.env`

#### **Gemini API Key**
1. Visit [AI Studio](https://aistudio.google.com)
2. Click "Get API key"
3. Create a new API key
4. Copy and add to `.env`

#### **Groq API Key**
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up/login
3. Navigate to API Keys section
4. Create a new API key
5. Copy and add to `.env`

#### **Hugging Face API Key**
1. Visit [huggingface.co](https://huggingface.co)
2. Sign up for an account
3. Go to Settings → Access Tokens
4. Create a new token (with read access)
5. Copy and add to `.env`

#### **Ollama API Key (Optional)**
1. Download [Ollama](https://ollama.com)
2. Install and run locally
3. Ollama runs on `http://localhost:11434` by default
4. No API key required for local setup (optional if using remote Ollama)

---

## Testing the Setup

### Test Individual APIs

Test each API to ensure your setup is correct:

#### **Test Cohere**
```bash
python cohere_example.py
```
When prompted, enter: `What is machine learning?`

#### **Test Gemini**
```bash
python gemini_example.py
```
When prompted, enter: `What is machine learning?`

#### **Test Groq**
```bash
python groq_example.py
```
When prompted, enter: `What is machine learning?`

#### **Test Hugging Face**
```bash
python huggingface_example.py
```
When prompted, enter: `What is machine learning?`

#### **Test Ollama (Local)**
First, ensure Ollama is running:
```bash
ollama serve
```

In another terminal:
```bash
python ollama_example.py
```
When prompted, enter: `What is machine learning?`

### Expected Output

Each script should return a response from the respective API. Example:
```
Enter prompt: What is machine learning?
Machine learning is a subset of artificial intelligence...
```

---

## Troubleshooting

### Issue: "API key not found!"

**Solution:**
- Ensure `.env` file is in the correct location (project root)
- Check that you've correctly added the API key
- Verify variable names match exactly (case-sensitive on Linux/macOS)
- Make sure there are no spaces around the `=` sign

### Issue: "ModuleNotFoundError" when importing packages

**Solution:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again
- Try: `pip install --upgrade pip`

### Issue: "Connection Error" or "Timeout"

**Solution:**
- Check your internet connection
- Verify the API service is operational (check their status pages)
- Check if API key has the right permissions
- Try again after a few seconds

### Issue: "Invalid API Key"

**Solution:**
- Double-check your API key in the `.env` file
- Ensure no extra spaces or characters
- Regenerate the API key from the provider's dashboard
- Verify the key hasn't expired

### Issue: Ollama connection failed

**Solution:**
- Ensure Ollama is installed: [ollama.com](https://ollama.com)
- Start Ollama service:
  ```bash
  ollama serve
  ```
- Pull the required model:
  ```bash
  ollama pull llama3
  ```
- Check if service is running on `http://localhost:11434`

### Issue: Mixed API responses or errors

**Solution:**
- Check the API rate limits haven't been exceeded
- Review the error message returned by the API
- Check API documentation for model availability in your region
- Ensure you have sufficient credits/quota on your account

---

## Next Steps

Once setup is complete:

1. Modify the example scripts for your use case
2. Adjust model parameters (temperature, max_tokens, etc.)
3. Implement error handling as needed
4. Build your application on top of these examples

For more information, refer to:
- [README.md](README.md) - Project overview
- Individual API documentation links in the README

---

## Getting Help

If you encounter issues:
1. Check the Troubleshooting section above
2. Review the API provider's documentation
3. Check your `.env` file configuration
4. Ensure all dependencies are installed: `pip list`

Happy coding!
