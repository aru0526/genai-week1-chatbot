import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.5-flash",  # agar error aaye toh neeche dekho
    contents="Explain what an API is in 3 simple lines.",
)

print(response.text)