

from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Automatically loads .env from the current directory
load_dotenv()  # or use full path: load_dotenv(dotenv_path="D:/GEN AI/code from self/langchain/.env")

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

# Debug check
if api_key is None:
    print("❌ API key not loaded! Check .env file and path.")
else:
    print("✅ API key loaded.")

# Use it
llm = OpenAI(model='gpt-3.5-turbo-instruct', openai_api_key=api_key)
result = llm.invoke("What is the capital of Bangladesh?")
print(result)