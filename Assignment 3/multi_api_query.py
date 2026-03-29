from openai_example import query_openai
from groq_example import query_groq
from ollama_example import query_ollama
from huggingface_example import query_huggingface
from gemini_example import query_gemini
from cohere_example import query_cohere


providers = {
    "1": ("OpenAI", query_openai),
    "2": ("Groq", query_groq),
    "3": ("Ollama", query_ollama),
    "4": ("HuggingFace", query_huggingface),
    "5": ("Gemini", query_gemini),
    "6": ("Cohere", query_cohere)
}


print("Select AI Provider")

for key, value in providers.items():
    print(f"{key}. {value[0]}")


choice = input("Enter choice: ")

prompt = input("Enter your prompt: ")

if choice in providers:

    name, func = providers[choice]

    print(f"\nQuerying {name}...\n")

    result = func(prompt)

    print(result)

else:

    print("Invalid choice")