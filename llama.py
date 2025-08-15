from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os

os.environ["OPENAI_API_KEY"] = "ENTER_API_KEY"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "ENTER_API_KEY"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "I am chatbot. I am here to help you. Please type your queries"),
        ("user", "Question:{question}")
    ]
)

st.title("LLaMA ChatBot")
input_text = st.text_input("I am LLaMA ChatBot. How may I help you")

llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))