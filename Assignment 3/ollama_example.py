import requests


def query_ollama(prompt):

    try:

        url = "http://localhost:11434/api/generate"

        data = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=data)

        return response.json()["response"]

    except Exception as e:

        return f"Error: {str(e)}"


if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("Querying Ollama...\n")

    result = query_ollama(user_prompt)

    print("Response:")
    print(result)