import os
from dotenv import load_dotenv
import google.generativeai as genai
from horror import build_prompt

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_horror_story(name, situation, num_lines):
    prompt = build_prompt(name, situation, num_lines)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response and response.text else "❌ Failed to generate story."
