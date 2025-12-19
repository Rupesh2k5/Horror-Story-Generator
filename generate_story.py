import os
from google import genai
from horror import build_prompt

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_horror_story(name, situation, num_lines):
    prompt = build_prompt(name, situation, num_lines)

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text
