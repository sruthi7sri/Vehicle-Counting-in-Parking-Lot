import streamlit as st
import cv2
import tempfile
from tensorflow.keras.models import load_model
import numpy as np
import os

st.title("🚗 Vehicle Counting in Parking Lot")

# Load model (update path if needed)
MODEL_PATH = "model_final.h5"
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    st.error("Model file not found. Please ensure model_final.h5 is present.")

uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

if uploaded_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    cap = cv2.VideoCapture(tfile.name)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize or preprocess frame if needed by model
        # For now, we'll just display it
        stframe.image(frame, channels="BGR", use_column_width=True)

    cap.release()
