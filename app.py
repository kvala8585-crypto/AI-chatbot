from fastapi import FastAPI
from chatbot import get_answer   # local function

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Chatbot Running"}

@app.post("/chat/")
def chat(query: str):
    try:
        # 🔥 Local chatbot logic (NO API KEY)
        response = get_answer(query)

        return {
            "response": response
        }

    except Exception as e:
        return {
            "error": str(e)
        }