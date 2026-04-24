<<<<<<< HEAD
from langchain_openai import ChatOpenAI
from rag import load_vector_db
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
d#ef get_answer(query):
    #return "This is test response"


def get_answer(query):
    try:
         return "This is test response"
        # Load DB inside function (important)
        db = load_vector_db()
        api_key=os.getenv("OPENAI_API_KEY")
        print("API KEY:", api_key)
        print(get_answer(query))            

        # Initialize LLM
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=api_key
        )
        # Search similar docs
        docs = db.similarity_search(query)

        # Safe context join
        context = " ".join([doc.page_content for doc in docs]) if docs else "No data found"

        prompt = f"""
        Answer based on context:
        {context}

        Question: {query}
        """

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:
=======
from langchain_openai import ChatOpenAI
from rag import load_vector_db
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
d#ef get_answer(query):
    #return "This is test response"


def get_answer(query):
    try:
         return "This is test response"
        # Load DB inside function (important)
        db = load_vector_db()
        api_key=os.getenv("OPENAI_API_KEY")
        print("API KEY:", api_key)
        print(get_answer(query))            

        # Initialize LLM
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=api_key
        )
        # Search similar docs
        docs = db.similarity_search(query)

        # Safe context join
        context = " ".join([doc.page_content for doc in docs]) if docs else "No data found"

        prompt = f"""
        Answer based on context:
        {context}

        Question: {query}
        """

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:
>>>>>>> b743e97ac53eed842df7b2eb242dd75461ff4ca1
        return f"Error: {str(e)}"