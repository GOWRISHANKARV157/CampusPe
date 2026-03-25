import requests

try:
    user_input = input("Enter your prompt: ")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user_input
        }
    )

    data = response.json()
    print("\nResponse:")
    print(data['response'])

except Exception as e:
    print("Error:", e)