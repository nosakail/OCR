import streamlit as st



st.set_page_config(layout="wide", page_title="Image analysis using OCR")

st.write("## Find text in your image ")
st.write("this is the description")


st.sidebar.write("## Upload and download :gear:")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
