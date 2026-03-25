import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3", 
                "prompt": prompt,
                "stream": False  
            }
        )

        data = response.json()

        if "error" in data:
            return f"Ollama Error: {data['error']}"

        return data.get("response", "No response")

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print(query_ollama(prompt))