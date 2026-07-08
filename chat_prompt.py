import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatAnthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    model="claude-haiku-4-5"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Tell me about {topic}.")
])

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({
    "domain": "healthcare",
    "topic": "cancer"
})

print(response)