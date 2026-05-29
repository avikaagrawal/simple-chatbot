import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer
nltk.download('punkt')
nltk.download('punkt_tab')

# Title
st.title("Simple AI Chatbot")

# Responses
responses = {
    "hello": "Hi! How can I help you?",
    "hey": "Hello! Nice to meet you.",
    "python": "Python is a popular programming language.",
    "bca": "BCA stands for Bachelor of Computer Applications.",
    "internship": "Internships help students gain real-world experience.",
    "ai": "AI stands for Artificial Intelligence.",
    "bye": "Goodbye! Have a great day!"
}

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Tokenize input
    words = word_tokenize(user_input.lower())

    bot_reply = "Sorry, I don't understand that."

    for word in words:
        if word in responses:
            bot_reply = responses[word]
            break

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })