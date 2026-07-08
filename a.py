import streamlit as st
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

st.title("College Research Assistant")

college = st.text_input("Enter a college or university name")

model = ChatAnthropic(model="claude-haiku-4-5")

if st.button("Submit") and college:

    prompt = f"""
You are a College Research Assistant.

User input: "{college}"

Rules:
1. First decide whether the input is a real college or university.
2. If it is a college/university:
   - Give a brief overview.
   - Then answer the user's request if they asked anything specific.
3. If it is NOT a college or university, politely reply:
   "Sorry, I can only provide information about colleges and universities. '{college}' doesn't appear to be one."

Do not provide any information about non-college topics.
"""

    result = model.invoke(prompt)

    st.write(result.content)