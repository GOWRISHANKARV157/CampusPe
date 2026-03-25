import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    user_input = input("Enter your prompt: ")

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": user_input}]
    )

    print("\nResponse:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)