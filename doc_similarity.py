from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os


load_dotenv()

os.environ["OPENAI_API_KEY"] = "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"  # replace with your key


embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)