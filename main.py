import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
import os
import dotenv
st.title("College Research Assistant")
dotenv.load_dotenv()
parse_response = StrOutputParser()
college = st.selectbox(
    "Select a college or university:",
    [
        "Harvard University",
        "Stanford University",
        "Massachusetts Institute of Technology (MIT)",
        "University of California, Berkeley",
        "University of Oxford",
        "University of Cambridge",
        "California Institute of Technology (Caltech)",
        "Princeton University",
        "Yale University",
        "Columbia University"
    ]
)
lines = st.selectbox(
    "Select the number of lines for the response:",
    [1, 2, 3, 4, 5,6,7,8,]
)
#prompt = f"Please provide a detailed response to the following prompt: {college}"
prompt_template = PromptTemplate(
    input_variables=["college", "lines"],
    template="You are a College Research Assistant. Please provide a detailed response to the following prompt: {college} (Limit your response to {lines} lines.)"
)
output_parser = StrOutputParser()
prompt = prompt_template.invoke({
    "college": college,
    "lines": lines})
model = ChatAnthropic(model="claude-haiku-4-5")
if st.button("Submit"):
    response = model.invoke(prompt)
    result = output_parser.invoke(response)
    st.write(result)