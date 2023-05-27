import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

#start the camera and take the picture
with st.expander("start Camera"):
    camera_image= st.camera_input("Camera")

if camera_image:
    #Create the pillow image
    img = Image.open(camera_image)
    #convert pillow image to grayscale(Black and White)
    gray_img = img.convert("L")

    #Display the black and white image
    st.image(gray_img)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_upload = img.convert("L")
    st.image(gray_upload)