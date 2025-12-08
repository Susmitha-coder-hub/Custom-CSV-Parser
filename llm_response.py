# llm_response.py
import os
from openai import OpenAI

# Get API key from environment variable (never hardcode!)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set!")

client = OpenAI(api_key=api_key)

def generate_response(prompt: str) -> str:
    """
    Send a prompt to the LLM and get the response.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
