import easyocr
import cv2
import numpy as np
import streamlit as st
from io import BytesIO
from PIL import Image
from processing import process_not_darkened_background
from processing import process_background_darkened
from processing import ajust_low_contrast
from processing import ajust_hight_saturation
    
#keep best ocr result and show image
def apply_best_result(img_path, imp_img_path):  
    reader = easyocr.Reader(['en'], gpu=False)

    base_img = cv2.imread(img_path)
    imp_img = cv2.imread(imp_img_path)
    
    results = reader.readtext(base_img)
    results2 = reader.readtext(imp_img)
    
    performance_base_img = np.mean([r[2] for r in results])
    performance_imp_img = np.mean([r[2] for r in results2])
    
    if performance_base_img > performance_imp_img:
        for result in results:
            bbox, res, score = result
            
            # Conversion
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
        # Convert image in RGB (OpenCV read image in BGR by default)
        annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
        return annotated_img
        
    else :
        for result in results2:
            bbox, res, score = result
            
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
        annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
        return annotated_img



# Download the fixed image
def convert_image(img_array):
    img_pil = Image.fromarray(img_array)
    buf = BytesIO()
    img_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im
    
def show(base_img, res_img_array, col1, col2):
    col1.write("Original Image :camera:")
    col1.image(base_img)

    col2.write("Text found :wrench:")
    # Convertir le tableau NumPy en une image PIL pour l'afficher
    res_img_pil = Image.fromarray(res_img_array)
    col2.image(res_img_pil)
    st.sidebar.markdown("\n")
    # Call convert fonction with numpy array
    st.sidebar.download_button("Download result", convert_image(res_img_array), "your_result_image.png", "image/png")


def dark_back(img_path):
    base_img = cv2.imread(img_path)
    img = process_not_darkened_background(img_path)
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(img)

    for result in results:
            bbox, res, score = result
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
    annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    return annotated_img

def light_back(img_path):
    base_img = cv2.imread(img_path)
    img = process_background_darkened(img_path)
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(img)

    for result in results:
            bbox, res, score = result
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
    annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    return annotated_img

def low_contrast(img_path):
    base_img = cv2.imread(img_path)
    img = ajust_low_contrast(img_path)
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(img)
    
    for result in results:
            bbox, res, score = result
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
    annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    return annotated_img

def hight_saturation(img_path):
    base_img = cv2.imread(img_path)
    img = ajust_hight_saturation(img_path)[0]
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(img)

    for result in results:
            bbox, res, score = result
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
    annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    return annotated_img
    
    


