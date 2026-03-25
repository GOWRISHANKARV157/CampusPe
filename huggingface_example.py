import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

api_key = os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(token=api_key)

def query_api(prompt):
    try:
        response = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )

        return response.choices[0].message.content

    except Exception as e:
        import traceback
        return f"Error: {traceback.format_exc()}"

if __name__ == "__main__":
    user_prompt = input("Enter prompt: ")
    print(query_api(user_prompt))