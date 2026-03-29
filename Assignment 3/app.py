import streamlit as st
import json
import os
from datetime import datetime
from openai_example import query_openai
from groq_example import query_groq
from ollama_example import query_ollama
from huggingface_example import query_huggingface
from gemini_example import query_gemini
from cohere_example import query_cohere
import time
import re


def is_structured(text: str) -> bool:
    # Detect bullets, numbered lists, or multiple sections
    bullet_or_number = re.search(r"(^\s*[-*•]\s+)|(^\s*\d+\.\s+)", text, re.MULTILINE)
    multiple_paragraphs = len([p for p in text.split("\n\n") if p.strip()]) >= 2
    return bool(bullet_or_number or multiple_paragraphs)

def now_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

HISTORY_FILE = "conversation_history.json"

providers = {
    "OpenAI": query_openai,
    "Groq": query_groq,
    "Ollama": query_ollama,
    "HuggingFace": query_huggingface,
    "Gemini": query_gemini,
    "Cohere": query_cohere
}

# ---------- Load History ----------

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

history = load_history()

# ---------- UI ----------

st.title("Multi-API AI Interface")

mode = st.radio(
    "Mode",
    ["Single Provider", "Compare Different Responses"]
)

prompt = st.text_area("Enter your prompt")

# ---------- Single Provider Mode ----------

if mode == "Single Provider":

    provider = st.selectbox("Select Provider", list(providers.keys()))

    if st.button("Generate Response"):

        func = providers[provider]

        result = func(prompt)

        st.subheader("Response")
        st.write(result)

        history.append({
            "timestamp": now_ts(),
            "provider": provider,
            "prompt": prompt,
            "response": result
        })

        save_history(history)

# ---------- Compare Responses Mode ----------

if mode == "Compare Different Responses":

    if st.button("Compare Responses"):

        results = {}
        metrics = []

        for name, func in providers.items():

            start = time.time()

            try:
                response = func(prompt)
            except Exception as e:
                response = f"Error: {str(e)}"

            elapsed = round(time.time() - start, 3)

            word_count = len(response.split())
            char_count = len(response)

            
            structured = is_structured(response)

            results[name] = response

            metrics.append({
                "API": name,
                "Response Time (s)": elapsed,
                "Word Count": word_count,
                "Characters": char_count,
                "Structured Output": "Yes" if structured else "No"
            })

        st.subheader("Responses from all APIs")

        for name, res in results.items():
            st.markdown(f"### {name}")
            st.write(res)

        st.subheader("Response Comparison")

        st.table(metrics)

        history.append({
            "timestamp": now_ts(),
            "provider": "comparison",
            "prompt": prompt,
            "response": results,
            "metrics": metrics
        })

        save_history(history)

# ---------- Streaming Example (Groq) ----------

st.divider()
st.subheader("Streaming Response (Groq)")

if st.button("Stream Response"):

    try:
        from groq import Groq
        import os
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        placeholder = st.empty()
        text = ""

        for chunk in stream:
            if chunk.choices[0].delta.content:
                text += chunk.choices[0].delta.content
                placeholder.markdown(text)

    except Exception as e:
        st.error(str(e))

# ---------- Conversation History ----------

st.divider()
st.subheader("Conversation History")

for item in reversed(history):

    timestamp = item.get("timestamp", "N/A")
    st.markdown(f"**Time:** {timestamp}")
    st.markdown(f"**Prompt:** {item['prompt']}")

    if item["provider"] == "comparison":
        st.markdown("**Compared Responses:**")
        for k,v in item["response"].items():
            st.markdown(f"**{k}:**")
            st.write(v)
    else:
        #st.markdown(f"**Time:** {item['timestamp']}")
        st.markdown(f"**Provider:** {item['provider']}")
        st.write(item["response"])

    st.markdown("---")