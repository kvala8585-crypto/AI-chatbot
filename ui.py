import streamlit as st
import requests

# Backend URL
API_URL = "http://127.0.0.1:8000/chat/"

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot (ChatGPT Style)")

# Chat history store
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call API
    try:
        response = requests.post(
            API_URL,
            params={"query": user_input}
        )

        result = response.json()
        bot_reply = result.get("response", "No response")

    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    # Show bot message
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})