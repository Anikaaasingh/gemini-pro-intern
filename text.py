from dotenv import load_dotenv
load_dotenv() ## loading env variables

import google.generativeai as genai
import streamlit as st
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## load gemini pro and get response
model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

def show_page1():
## set up streamlit app
   st.set_page_config(page_title="Q&A")
   st.header("Gemini LLM App")
   input=st.text_input("Input",key="input")
   submit=st.button("Ask the question")

## submit clicked
   if submit:
      response=get_gemini_response(input)
      st.subheader("The response is")
      st.write(response)
   