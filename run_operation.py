from utils import (read_video, 
                   save_video
                   )
from service import(draw_keypoints)
import numpy as np

def apply_func_to_video(video_name , operation):
     
    input_path = "data/" + video_name + ".mp4"
    output_path = "output/" + video_name+ ".avi"
    
    input_frames = read_video(input_path)
    output_frames = []

    for i, frame in enumerate(input_frames):

        print("Processing frame NO: " + str(i))
        # TODO: operation of video frames
        output_frames.append(operation(frame))

    print("No frames: " + str(len(input_frames)))
    print("Input Shape:" , input_frames[0].shape)
    print("Output Shape:" , output_frames[0].shape)
    save_video(output_frames, output_path)

if __name__ == '__main__':
    apply_func_to_video("test-1" , draw_keypoints)