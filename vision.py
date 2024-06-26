from dotenv import load_dotenv
load_dotenv()  # loading env variables
from PIL import Image

import google.generativeai as genai
import streamlit as st
import os

# Configure generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini pro and get response
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
        return response.text  # Ensure the response text is returned
    else:
        return "No input provided"  # Handle the case when input is empty
def show_page2():
# Set up Streamlit app
    st.set_page_config(page_title="Gemini Image demo")
    st.header("Gemini Image App")

    input = st.text_input("Input prompt", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    image = None  # Initialize image as None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about the image")

# If the ask button is clicked
    if submit:
        response = get_gemini_response(input, image)
        st.subheader("The Response is")
        st.write(response)
