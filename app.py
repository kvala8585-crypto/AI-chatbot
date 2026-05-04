from fastapi import FastAPI
from chatbot import get_answer   #  AI + fallback already handled here

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Chatbot Running 🚀"}

@app.get("/chat")
def chat(query: str):
    response = get_answer(query)

    return {
        "response": response
    }
