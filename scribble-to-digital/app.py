import streamlit as st
from utils.ocr_processor import extract_text
from utils.ai_processor import process_text
from PIL import Image

st.title("Scribble to Digital")

uploaded_file = st.file_uploader("Upload handwritten note")

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Convert"):

        text = extract_text(uploaded_file)

        st.subheader("Raw OCR Text")
        st.write(text)

        clean_text = process_text(text)

        st.subheader("AI Corrected Notes")
        st.write(clean_text)



st.title("Scribble to Digital Notes")

st.write("Upload an image of handwritten notes and convert it to digital text.")

uploaded_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image")
    st.write("Processing will appear here...")