import os
from dotenv import load_dotenv
import google.generativeai as genai
from horror import build_prompt

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_horror_story(name, situation, num_lines):
    # Build the story prompt
    prompt = build_prompt(name, situation, num_lines)

    # Use Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Return the generated story text
    return response.text if response and response.text else "❌ Failed to generate story."
