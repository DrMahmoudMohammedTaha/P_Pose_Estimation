import cv2
import os

def extract_frames(video_path: str, output_folder: str, frame_interval: int) -> list: 
    """
    This function takes a video path and cut it into frames to be used for training on yolo and save the output in 
    output_folder.
    Args:
        video_path (str): the path to the video
        output_folder (str): the folder to save the frames
        frame_interval (int): the interval in seconds to cut the video
    returns: 
        None 
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = cv2.VideoCapture(video_path)

    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    interval = int(frame_interval * fps)

    frame_number = 0
    saved_frame_count = 0

    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        
        if frame_number % interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count}.png")
            cv2.imwrite(frame_filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            saved_frame_count += 1
        
        frame_number += 1
        print(f"Processing Frame: {frame_number}")

    video.release()

if __name__ == '__main__':

    video_path = 'D:\Artificial Intelligence\Machine Learning\Computer Vision\P_DeepPPP\data\match.mp4'
    output_folder = 'D:\Artificial Intelligence\Machine Learning\Computer Vision\P_DeepPPP\data'
    frame_interval = 5  # seconds

    extract_frames(video_path, output_folder, frame_interval)
