import os
from dotenv import load_dotenv
import google.generativeai as genai

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Check your .env file.")

genai.configure(api_key=api_key)

def load_lamma_cpp(model_args=None):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    def gemini_llm(prompt):
        response = model.generate_content(prompt)
        return response.text

    return gemini_llm