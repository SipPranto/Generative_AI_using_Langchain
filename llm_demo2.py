from langchain_openai import OpenAI
import os

# Set the environment variable directly in code
os.environ["OPENAI_API_KEY"] = "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"  # replace with your key

# Now OpenAI() will read it correctly
llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of Bangladesh")

print(result)