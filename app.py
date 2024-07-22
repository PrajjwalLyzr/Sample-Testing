from lyzr import ChatBot
import os
from dotenv import load_dotenv; load_dotenv()
import streamlit as st


os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_KEY')

def chatBot():
    chatbot = ChatBot.pdf_chat(
        input_files=["physics.pdf"],
    )

    return chatbot


if __name__ == "__main__":
    st.header('Test App')
    question = st.text_input('Enter your question: ')
    if question is not None:
        if st.button('Get'):
            agent = chatBot()
            response = agent.chat(question)
            st.write(response.response)