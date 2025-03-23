import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the GOOGLE_API_KEY from the environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Configure the API key
genai.configure(api_key= google_api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

# Create a Streamlit app
st.title("Google Generative AI Demo")

# Add a text input for user queries
user_input = st.text_input("Ask me anything:")

# Generate and display the response when the user submits a query
if user_input:
    response = model.generate_content(user_input)
    st.write("Response:")
    st.write(response.text)