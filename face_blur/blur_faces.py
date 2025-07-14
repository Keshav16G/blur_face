
import cv2
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Face Blur App", layout="centered")
st.title("🕶️ Face Blur App (Streamlit Version)")

# Load OpenCV Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def blur_faces(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        img_bgr[y:y+h, x:x+w] = cv2.blur(img_bgr[y:y+h, x:x+w], (30, 30))
    return img_bgr

option = st.radio("Select input type:", ["Upload Image", "Use Webcam"])

if option == "Upload Image":
    uploaded = st.file_uploader("Upload an image file", type=['jpg', 'jpeg', 'png'])
    if uploaded is not None:
        file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        st.image(img, channels="BGR", caption="Original Image")

        if st.button("Blur Faces"):
            result = blur_faces(img.copy())
            st.image(result, channels="BGR", caption="Blurred Image")

elif option == "Use Webcam":
    st.warning("Ensure your webcam is enabled. Press 'Start' to begin streaming. Press 'Stop' to end.")
    run = st.checkbox("Start Webcam")
    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)
    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame.")
            break
        frame = blur_faces(frame)
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cap.release()
    st.button("Stop Webcam", on_click=lambda: cap.release())