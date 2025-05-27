from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

#load_dotenv()


os.environ["OPENAI_API_KEY"] = "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"  # replace with your key

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("Tell me a joke")

print(result.content)