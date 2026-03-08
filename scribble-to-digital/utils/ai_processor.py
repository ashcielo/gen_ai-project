import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def process_text(raw_text):

    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Clean and format the following handwritten OCR text.
    Correct spelling mistakes and organize it properly.

    Text:
    {raw_text}
    """

    response = model.generate_content(prompt)

    return response.text