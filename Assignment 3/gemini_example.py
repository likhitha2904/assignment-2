import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def query_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("Querying Gemini...\n")

    result = query_gemini(user_prompt)

    print("Response:")
    print(result)