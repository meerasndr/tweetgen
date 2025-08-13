from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
load_dotenv()

def llm_call(number, topic):
    gemini_model = ChatGoogleGenerativeAI(model= "gemini-1.5-flash-latest")

    # Prompt template
    tweet_template = "Give me {number} tweets on {topic}"
    tweet_prompt = PromptTemplate(template=tweet_template, input_variables = ['number', 'topic'])
    #tweet_template.format(number=5, topic="Fighter Jets of World War 2")
    # LLM Chain
    tweet_chain = tweet_prompt | gemini_model
    response = tweet_chain.invoke({"number": number, "topic": topic})
    return response

st.header("Tweet Generator")
st.subheader("Generate tweets on a topic of your choice!")
topic = st.text_input("Topic")
number = st.number_input("Number of Tweets", min_value=1, max_value=15, step=1)
if st.button("Generate!"):
    tweets = llm_call(number, topic)
    st.write(tweets.content)