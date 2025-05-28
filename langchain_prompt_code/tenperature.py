from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

os.environ['OPENAI_API_KEY']='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'



model = ChatOpenAI(model='gpt-4', temperature=1.5)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)