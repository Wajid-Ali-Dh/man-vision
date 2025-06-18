import cv2
from ultralytics import YOLO

class DefectDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)
        boxes = results[0].boxes.xyxy.cpu().numpy() if results[0].boxes else []
        scores = results[0].boxes.conf.cpu().numpy() if results[0].boxes else []
        classes = results[0].boxes.cls.cpu().numpy() if results[0].boxes else []
        return boxes, scores, classes
