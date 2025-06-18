import streamlit as st
import cv2
import numpy as np
import os
from defect_detector import DefectDetector
from decision_module import make_decision
from sensor_sim import get_sensor_data

st.set_page_config(page_title="AI Defect Detection Dashboard", layout="wide")
st.title("AI-Based Defect Detection and Adaptive Manufacturing Correction")


detector = DefectDetector()

# 
source = st.sidebar.selectbox("Input Source", ["Webcam", "Sample Image", "Sample Video"])

img_files = [f for f in os.listdir("sample_images") if f.lower().endswith((".jpg", ".png", ".jpeg"))]
video_file = st.sidebar.file_uploader("Upload a video file", type=["mp4", "avi", "mov"]) if source == "Sample Video" else None

if source == "Sample Image":
    if img_files:
        img_choice = st.sidebar.selectbox("Select Image", img_files)
        img_path = os.path.join("sample_images", img_choice)
        img = cv2.imread(img_path)
    else:
        st.warning("No images found in sample_images/.")
        img = None
    cap = None
elif source == "Sample Video" and video_file is not None:
    tfile = f"/tmp/{video_file.name}"
    with open(tfile, 'wb') as f:
        f.write(video_file.read())
    cap = cv2.VideoCapture(tfile)
    img = None
elif source == "Webcam":
    cap = cv2.VideoCapture(0)
    img = None
else:
    cap = None
    img = None

run = st.button("Start/Stop Simulation")
frame_placeholder = st.empty()
status_placeholder = st.empty()

while run:
    if cap is not None:
        ret, frame = cap.read()
        if not ret:
            st.warning("No frame available.")
            break
    elif img is not None:
        frame = img.copy()
    else:
        st.warning("No input selected.")
        break

    boxes, scores, classes = detector.detect(frame)
    sensor_data = get_sensor_data()
    status = make_decision(scores, sensor_data)

    # Draw boxes
    for box, score in zip(boxes, scores):
        x1, y1, x2, y2 = map(int, box)
        color = (0, 0, 255) if score > 0.5 else (0, 255, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"Defect: {score:.2f}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Show status
    status_placeholder.markdown(f"### System Status: **{status}**")
    frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

    if status != 'RUNNING':
        st.warning(f"System {status}! Action required.")
        break

    if cap is not None:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if cap is not None:
    cap.release()
    cv2.destroyAllWindows()
