import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

try:
    user_input = input("Enter your prompt: ")

    response = requests.post(API_URL, headers=headers, json={"inputs": user_input})

    print("\nResponse:")
    print(response.json())

except Exception as e:
    print("Error:", e)