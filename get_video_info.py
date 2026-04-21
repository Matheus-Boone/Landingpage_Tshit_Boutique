import cv2
import os

video_path = "video_scroll_final.mp4"
if not os.path.exists(video_path):
    print(f"Error: {video_path} not found.")
else:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        print(f"FPS: {fps}")
        print(f"Frame Count: {frame_count}")
        print(f"Duration: {duration}")
    cap.release()
