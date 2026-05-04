#  AI Chatbot Automation System

##  Project Overview

This project is an end-to-end **AI-powered chatbot automation system** built using FastAPI.

It is capable of handling real-time user queries, generating AI-based responses, storing interactions in a database, and optionally triggering automated email replies.

The system is designed with a **scalable backend architecture** and can be integrated with automation platforms like Zapier and n8n for real-world business workflows.

---

##  Live Demo

 **Deployed on:** :Render 
 **Live API URL:** https://ai-chatbot-5-m89t.onrender.com/

👉 Open the link in browser to verify service status  
👉 Use API tools (Postman / frontend) to test `/chat` endpoint  

---

##  Features

* AI-powered chatbot response system  
*  High-performance FastAPI backend  
*  Query & response logging using database  
*  Optional automated email responses  
*  Ready for Zapier / n8n integration  
*  Cloud deployment support (Render / Railway)  

---

##  Tech Stack

* **Backend:** FastAPI  
* **Language:** Python  
* **Database:** SQLite  
* **Server:** Uvicorn  
* **Automation:** n8n 
* **Deployment:** Render  

---

## Project Structure
AI Chatbot/
│
├── app.py # Main FastAPI application
├── chatbot.py # AI response logic
├── database.py # Database operations
├── email_service.py # Email automation logic
├── requirements.txt # Dependencies
├── Procfile # Deployment config
├── .gitignore # Ignore sensitive files

---

## Installation & Setup

### Clone Repository
https://github.com/kvala8585-crypto/AI-chatbot/edit/main/README.md

cd AI Chatbot


###  Install Dependencies
pip install -r requirements.txt



###  Setup Environment Variables


---

## Run Locally
uvicorn app:app --reload


##  API Endpoints

###  Health Check
GET /

✅ Returns service status  
Example:

{
"message": "AI Chatbot Running 🚀"
}

---

###  Chat Endpoint
POST /chat/


#### Parameters:

* `query` → User input (required)  
* `email` → Optional (for automated email response)


## Automation Integration

This system supports integration with:

* n8n  

###  Workflow:

User → Automation Tool → API → AI Processing → Database → Email Response  

---

### Steps:

1. Push code to GitHub  
2. Connect repository to Render  
3. Configure environment variables  
4. Deploy using Uvicorn server  

## Use Cases

* Customer Support Chatbot  
* Automated Email Responder  
* Lead Generation System  
* AI-based Query Handling  

---

##  Author

Kavi Vala 
AI automation  

## Future Improvements

* Add frontend UI (React / HTML)  
* Enhance conversation memory  
* Multi-language support  
* Authentication & user sessions  
* Deploy full-stack version  

---
