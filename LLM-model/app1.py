from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Styling
st.markdown("""
<style>
body {
    font-family: 'Roboto', sans-serif;
    background-color: #f0f2f6; 
    color: #333; 
}

.title {
    text-align: center;
    font-size: 48px;
    color: #2980b9; 
    margin-bottom: 40px;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1); 
}

.container {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2); 
    padding: 40px;
    border-radius: 20px; 
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15); 
}

.stTextInput > div > div > input {
    font-size: 20px; 
    padding: 15px; 
    border: 1px solid #ccc;
    border-radius: 10px; 
    width: calc(100% - 30px);
    box-sizing: border-box;
    transition: border-color 0.3s;
}

.stTextInput > div > div > input:focus {
    border-color: #2980b9; 
    outline: none;
}

.stButton button {
    background-color: #2980b9; 
    color: white;
    padding: 15px 30px;
    border: none;
    border-radius: 10px; 
    cursor: pointer;
    font-size: 18px;
    transition: background-color 0.3s; 
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.stButton button:hover {
    background-color: #2471a3; 
}

.response-container {
    background-color: #fff;
    padding: 30px;
    border-radius: 15px; 
    margin-top: 40px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15); 
}

.response-container p {
    font-size: 20px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# Initialize Streamlit app
st.markdown('<p class="title">Gemini LLM Application</p>', unsafe_allow_html=True)

# Main content container
with st.container():
    input_text = st.text_input("Input:", key="input")
    col1, col2 = st.columns([3, 1]) 

    with col1:
        submit_button = st.button("Ask the question")

    with col2:
        clear_button = st.button("Clear")

    # When submit is clicked
    if submit_button and input_text:
        with st.spinner("Generating response..."):
            response = get_gemini_response(input_text)

        # Display response in a styled container
        st.markdown(f'<div class="response-container"><p>{response}</p></div>', unsafe_allow_html=True)

    # When clear is clicked
    if clear_button:
        st.session_state['input'] = "" 
        st.experimental_rerun()
