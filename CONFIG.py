
import os
from dotenv import load_dotenv
#load .env file
load_dotenv()
#get enviroment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
#dwbung check
if OPENAI_API_KEY is None:
    print("ERROR: OPENAI_API_KEY not found in .env file")
else:
    print("API key loaded successfully")
