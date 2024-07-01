import google.generativeai as genai

from config import config

genai.configure(api_key=config["google_api_key"])
model = genai.GenerativeModel('gemini-1.5-flash')


def generate_content(input_str: str) -> str:
    response = model.generate_content(input_str)
    return response.text
