from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

os.environ['OPENAI_API_KEY']='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'



model = ChatOpenAI()

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)