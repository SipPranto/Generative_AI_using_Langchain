from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st
import os

os.environ['OPENAI_API_KEY']='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'


model = ChatOpenAI()

st.header('Reasearch Tool')

user_input=st.text_input('Enter your prompt')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.text(result.content)
