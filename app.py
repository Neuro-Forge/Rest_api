import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the Gemini API with your key
genai.configure(api_key="AIzaSyAumH0LCaGl3TkTGRqkNmmwk-bSdCRvZ34")


def get_gemini_response(input_text, image):
    # Added "models/" prefix to fix the 404 error
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

## Initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Google Lens")
input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Updated to use modern Streamlit parameter
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me about the image")

## If ask button is clicked
if submit:
    # Check if an image actually exists before making the API call
    if image is not None:
        with st.spinner("Analyzing image..."):
            response = get_gemini_response(input_prompt, image)
            st.subheader("The Response is")
            st.write(response)
    else:
        st.error("Please upload an image first!")