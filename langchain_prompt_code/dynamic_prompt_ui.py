from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
import os

os.environ['OPENAI_API_KEY']='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'
model = ChatOpenAI()

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )



template = PromptTemplate(
    template="""Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
   - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
input_variables=['paper_input','style_input','length_input']

)

prompt=template.invoke({
'paper_input':paper_input,
'style_input':style_input,
'length_input':length_input}
)


if st.button('Summarize'):
    result=model.invoke(prompt)

    st.write(result.content)