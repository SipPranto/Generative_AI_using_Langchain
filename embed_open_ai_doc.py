from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os




os.environ["OPENAI_API_KEY"] = "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"  # replace with your key

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)


documents = [
    "Dhaka is the capital of BD",
    "Delhi  is the capital of India",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))
print(len(result))