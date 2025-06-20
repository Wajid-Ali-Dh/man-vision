 # AI-Based Defect Detection and Adaptive Manufacturing Correction System

This project demonstrates a real-time computer vision pipeline for defect detection in manufacturing, with adaptive decision-making and a visual dashboard.

## Demo: Simulation Video
![Simulation Demo](simulation.gif)
## Features
- **Defect Detection:** Uses YOLOv8 for detecting defects (scratches, tool wear, misalignment) in images, video, or webcam feed.
- **Decision Module:** Rule-based logic to simulate pausing or correcting the process based on defect confidence and simulated sensor data.
- **Sensor Fusion:** Simulates IMU/encoder data for robust decision-making.
- **Visualization:** Streamlit dashboard for live visualization, status display, and user interaction.

## Project Structure
```
man-vision/
├── app.py                # Main Streamlit dashboard
├── defect_detector.py    # YOLOv8 wrapper for defect detection
├── decision_module.py    # Rule-based decision logic
├── sensor_sim.py         # Simulated IMU/encoder data
├── requirements.txt      # Python dependencies
├── sample_images/        # Place your test images here
│   └── ...
└── yolov8n.pt            # YOLOv8 model weights 
```

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Wajid-Ali-Dh/man-vision
cd man-vision
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Test Images or Videos
- Place images of defective and correct parts in `sample_images/`.
- (Optional) Prepare a video file for upload in the dashboard.

### 4. Run the Dashboard
```bash
streamlit run app.py
```
- Use the sidebar to select input source: Webcam, Sample Image, or Sample Video.
- For images, select from the dropdown. For video, upload your file.
- The dashboard will display predictions and system status.

 
---
**Developed for smart manufacturing, predictive maintenance, and visual inspection research.**
