from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
import streamlit as st 

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("human", "Question : {question}"),
    ]
)

## Streamlit framework

col1, col2, col3 = st.columns(3)
with col2 :
    st.image(r"C:/Users/admin/Chinmay/LangChain/KRISH_NAIK/FIRST/openai_logo.png", width=210)

st.markdown("<h1 style='text-align: center;'>FUN FACT GENERATOR</h1>", unsafe_allow_html=True)
# st.title("FUN FACT GENERATOR")
input_text = st.text_input("Ask away any fun facts :)")

##Open AI LLM

llm = ChatOpenAI(model = "gpt-4o-mini")
output_parser = StrOutputParser()
chain = prompt | llm | StrOutputParser()

if input_text :
    st.write(chain.invoke({'question' : input_text}))