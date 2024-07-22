from lyzr import ChatBot
import os
from dotenv import load_dotenv; load_dotenv()
import streamlit as st


os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_KEY')

def chatBot():
    chatbot = ChatBot.pdf_chat(
        input_files=["/content/sample_data/physics.pdf"],
    )

    return chatbot


if __name__ == "__main__":
    st.header('Test App')
    question = st.text_input('Enter your question: ')
    agent = chatBot()
    response = agent.chat("What is reflection")
    if st.button('Get'):
        st.write(response.response)