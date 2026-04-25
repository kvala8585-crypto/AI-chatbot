import os
from dotenv import load_dotenv

load_dotenv()

USE_OPENAI = os.getenv("OPENAI_API_KEY") is not None

if USE_OPENAI:
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )

def local_answer(query):
    query = query.lower()

    if "hello" in query:
        return "Hello! Kem cho? 😊"

    elif "ai" in query:
        return "AI is artificial intelligence 🤖"

    return "This is a fallback response (no API key)."

def get_answer(query):
    try:
        if USE_OPENAI:
            response = llm.invoke(query)
            return response.content
        else:
            return local_answer(query)

    except Exception as e:
        return local_answer(query)