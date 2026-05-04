import streamlit as st
import requests

#  Correct Backend URL (no trailing slash)
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot (ChatGPT Style)")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#  Input box
user_input = st.chat_input("Ask something...")

if user_input:
    #  Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    #  Call FastAPI backend
    try:
        response = requests.get(
            API_URL,
            params={"query": user_input}
        )

        if response.status_code == 200:
            data = response.json()
            bot_reply = data.get("response", "No response")
        else:
            bot_reply = f"Error: Status code {response.status_code}"

    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    # 👉 Show bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
