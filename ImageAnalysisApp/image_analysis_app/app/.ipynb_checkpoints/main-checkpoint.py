import streamlit as st
import os
import postprocessing
import time
from processing import improve_image
from postprocessing import apply_best_result
from postprocessing import show 
from PIL import Image
#import cv2

def delete_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
st.set_page_config(layout="wide", page_title="Image analysis using OCR")

st.write("## Find text in your image ")
st.write("this is the description")


st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

upload_dir = 'uploaded_image'
img_to_process_dir = 'img_to_process'

if my_upload == None:
    base_img = Image.open('img_example/image002.jpg')
    imp_img = Image.open('img_example/ocr_result.png')
    
    col1.write("Original Image :camera:")
    col1.image(base_img)
    col2.write("Fixed Image :wrench:")
    col2.image(imp_img)
    col1.markdown('<p style="font-size:24px;">Try with your image &#x2B06;</p>', unsafe_allow_html=True)

    
    
else :
    progress_bar = st.progress(0)

    delete_files_in_directory(upload_dir)
    delete_files_in_directory(img_to_process_dir)
    
    # Générer un nom unique pour l'image
    file_name = os.path.join(upload_dir, f"image_{int(time.time())}.{my_upload.name.split('.')[-1]}")
    with open(file_name, "wb") as f:
        f.write(my_upload.getbuffer())
    img_path = os.path.abspath(file_name)

    progress_bar.progress(33)
    
    file_name_without_extension = os.path.splitext(os.path.basename(file_name))[0]
    
    improve_image(img_path)
    imp_img_path = os.path.join(img_to_process_dir, file_name_without_extension + '_result.png')
    
    print(imp_img_path)
    print(img_path)
    #print(file_name)
    #print(file_name_without_extension)
    base_img = Image.open(img_path)

    progress_bar.progress(66)
    
    res_img = apply_best_result(img_path, imp_img_path)
    
    progress_bar.progress(90)
    
    show(base_img, res_img, col1, col2)

    progress_bar.progress(100)

    
    progress_bar.empty()
