import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_response(user_input):
    prompt = f"""
    A student says:
    "{user_input}"

    Respond as a supportive learning assistant.
    Explain the likely emotion and suggest practical study tips.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
    