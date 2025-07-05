import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }
)

def generate_horror_story(character_name, situation, no_of_lines):
    prompt = (
        f"Write a horror story of around {no_of_lines} lines.\n"
        f"The main character is {character_name}.\n"
        f"The story is set in this situation: {situation}.\n"
        f"Include suspense, creepy atmosphere, and a twist ending."
    )

    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text