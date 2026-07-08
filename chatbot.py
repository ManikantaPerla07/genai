from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    model = "claude-haiku-4-5"
    )

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = anthropic.invoke(user_input)
    print(f"Anthropic: {response.content}") 


