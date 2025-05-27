from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os


os.environ['HUGGINGFACEHUB_ACCESS_TOKEN']='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'

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)






model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Bangladesh?")

print(result.content)