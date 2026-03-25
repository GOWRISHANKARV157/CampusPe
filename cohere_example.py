import os
import cohere
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key)

def query_api(prompt):
    try:
        response = co.chat(
            model="command-xlarge-nightly",
            message=prompt,
            max_tokens=200,
            temperature=0.7
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter prompt: ")
    print(query_api(user_prompt))