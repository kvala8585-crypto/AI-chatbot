<<<<<<< HEAD
from fastapi import FastAPI 
from CONFIG import OPENAI_API_KEY
from openai import OpenAI
from chatbot import get_answer
from database import save_log
from email_service import send_email

app = FastAPI()
client = OpenAI(api_key=OPENAI_API_KEY)

@app.get("/")
def home():
    return {"message": "AI Chatbot Running"}

@app.post("/chat/")
def chat(query: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user", "content": query
            }]
        )
        return{"response": response.choices[0].message.content}
    except Exception as e:
        return{"error":str(e)}


    #save_log(query, response)

    #if email:
        # pass   # send_email(email, response) temporarily bandh
    #if email:
        #send_email(email, response)

    #return {
       # "query": query,
       # "response": response
=======
from fastapi import FastAPI 
from CONFIG import OPENAI_API_KEY
from openai import OpenAI
from chatbot import get_answer
from database import save_log
from email_service import send_email

app = FastAPI()
client = OpenAI(api_key=OPENAI_API_KEY)

@app.get("/")
def home():
    return {"message": "AI Chatbot Running"}

@app.post("/chat/")
def chat(query: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user", "content": query
            }]
        )
        return{"response": response.choices[0].message.content}
    except Exception as e:
        return{"error":str(e)}


    #save_log(query, response)

    #if email:
        # pass   # send_email(email, response) temporarily bandh
    #if email:
        #send_email(email, response)

    #return {
       # "query": query,
       # "response": response
>>>>>>> b743e97ac53eed842df7b2eb242dd75461ff4ca1
    #}