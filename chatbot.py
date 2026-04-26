import os
from dotenv import load_dotenv
from google import genai   # ✅ NEW package

load_dotenv()

# 🔑 API key (correct name use kar)
API_KEY = os.getenv("GEMINI_API_KEY")


USE_AI = API_KEY is not None
print("USE_AI:", USE_AI)

# 🤖 Gemini setup
if USE_AI:
    client = genai.Client(api_key=API_KEY)

def local_answer(query):
    query = query.lower()

    if "hello" in query:
        return "Hello! Kem cho? 😊"
    elif "ai" in query:
        return "AI is artificial intelligence 🤖"

    return "Fallback response"

def get_answer(query):
    try:
        if USE_AI:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=query
            )
            return response.text
        else:
            return local_answer(query)

    except Exception as e:
        print("ERROR:", e)
        return local_answer(query)