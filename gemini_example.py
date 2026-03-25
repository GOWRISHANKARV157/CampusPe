import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("API key not found!")
    exit()
genai.configure(api_key=api_key)
def query_api(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    user_prompt = input("Enter prompt: ")
    print(query_api(user_prompt))