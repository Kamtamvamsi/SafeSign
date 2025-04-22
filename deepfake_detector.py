# Deepfake detection module
import cv2
import numpy as np
import random
from moviepy.video import VideoClip

def extract_random_frame(video_path):
    clip = video_path(video_path)
    duration = int(clip.duration)
    frame_time = random.randint(1, max(duration - 1, 1))
    frame = clip.get_frame(frame_time)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame

def simulate_model_prediction(frame):
    # Simulate deepfake detection with random output
    score = round(random.uniform(60.0, 99.0), 2)
    label = "FAKE" if score > 80 else "REAL"
    return label, score

def detect_deepfake(video_path):
    try:
        frame = extract_random_frame(video_path)
        label, score = simulate_model_prediction(frame)
        return label, score
    except Exception as e:
        print(f"[ERROR] Deepfake Detection: {e}")
        return "UNKNOWN", 0.0
