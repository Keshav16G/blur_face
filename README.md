# blur_face
#  Face Blur App using OpenCV + Streamlit

This app allows you to automatically **detect and blur faces** in an uploaded image using OpenCV's Haar Cascades. Built with **Streamlit** for a fast, interactive UI.

##  Demo

###  Video
![Watch the Demo](demo/demo_video.mp4)

###  Screenshot
![App Screenshot](demo/demo_screenshot.png)

---

##  Features

- Upload any image (`.jpg`, `.png`, `.jpeg`)
- Automatically detects human faces using OpenCV Haar cascades
- Blurs the detected faces using Gaussian Blur
- Displays original and blurred versions side-by-side

---

##  Tech Stack

- 🧠 OpenCV for face detection and blurring
- ⚙️ Streamlit for the web app UI
- 📦 Python 3.7+

---

##  Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/face-blur-streamlit.git
cd face-blur-streamlit
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_face_blur.py

