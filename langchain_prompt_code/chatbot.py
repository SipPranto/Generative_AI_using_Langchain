from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

os.environ['OPENAI_API_KEY']='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'

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)