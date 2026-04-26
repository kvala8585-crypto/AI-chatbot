import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load env variables
load_dotenv()

# 🔑 API key load karo (FIRST)
API_KEY = os.getenv("GEMINI_API_KEY")

USE_AI = API_KEY is not None
print("USE_AI:", USE_AI)

# 🤖 Gemini setup
if USE_AI:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

# 🔹 Local fallback
def local_answer(query):
    query = query.lower()

    if "hello" in query:
        return "Hello! Kem cho? 😊"
    elif "ai" in query:
        return "AI is artificial intelligence 🤖"

    return "Fallback response"

# 🔹 Main function
def get_answer(query):
    try:
        if USE_AI:
            response = model.generate_content(query)
            return response.text
        else:
            return local_answer(query)

    except Exception as e:
        print("ERROR:", e)
        return local_answer(query)