from fastapi import FastAPI
from chatbot import get_answer   # local fallback
import google.generativeai as genai
import os

app = FastAPI()

# 🔑 Gemini API key (temporarily direct)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# 🤖 Model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.get("/")
def home():
    return {"message": "AI Chatbot Running"}

@app.get("/chat")
def chat(query: str):
    try:
        # 🔥 Gemini AI response
        ai_response = model.generate_content(query)

        return {
            "response": ai_response.text
        }

    except Exception as e:
        # 🔁 fallback to local logic
        fallback = get_answer(query)

        return {
            "response": fallback,
            "note": "Fallback response (AI failed)"
        }