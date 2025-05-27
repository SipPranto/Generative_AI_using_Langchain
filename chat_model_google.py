from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['GOOGLE_API_KEY']="AIzaSyDa2OwaEtQTKNj5_8sOTG-YthgUbtVeUoo"

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('What is the capital of Bangladesh')

print(result.content)