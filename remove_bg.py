import streamlit as st
import os
from PIL import Image 
from rembg import remove 

st.title("AI Background Remover")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(image, use_column_width=True)
    
    if st.button("Remove Background"):
        with st.spinner("Removing Background..."):
            output = remove(image)
        st.subheader("Background Removed")
        st.image(output, use_column_width=True)