import streamlit as st
import os
import postprocessing
import time

st.set_page_config(layout="wide", page_title="Image analysis using OCR")

st.write("## Find text in your image ")
st.write("this is the description")


st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

upload_dir = 'uploaded_image'
img_to_process_dir = 'img_to_process'

# Générer un nom unique pour l'image
file_name = os.path.join(upload_dir, f"image_{int(time.time())}.{my_upload.name.split('.')[-1]}")
with open(file_name, "wb") as f:
    f.write(my_upload.getbuffer())
img_path = os.path.abspath(file_name)

improve_image(img_path)
imp_img_path = os.path.join(img_to_process_dir, file_name + '_result.png')

res_image = apply_best_result(img_path, imp_img_path)
show(base_img, res_img)
