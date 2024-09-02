import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames


def save_video(frames, video_path):
    height, width,layers = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 30, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()
    print(f'Video saved to {video_path}')


# not fully working
def save_video_gray(frames, video_path):
    height, width = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 30, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()
    print(f'Video saved to {video_path}')

def apply_func_to_video(video_name , operations):
     
    input_path = "data/" + video_name + ".mp4"
    output_path = "output/" + video_name+ ".avi"
    
    input_frames = read_video(input_path)
    output_frames = []

    for i, frame in enumerate(input_frames):

        print("Processing frame NO: " + str(i))
        # TODO: operation of video frames
        for operation in operations:
            output_frames.append(operation(frame))

    print("No frames: " + str(len(input_frames)))
    print("Input Shape:" , input_frames[0].shape)
    print("Output Shape:" , output_frames[0].shape)
    save_video(output_frames, output_path)

def process_video(video_name , operations):
     
    input_path = "data/" + video_name + ".mp4"
    
    input_frames = read_video(input_path)
    output_frames = []

    for i, frame in enumerate(input_frames):

        print("Processing frame NO: " + str(i))
        # TODO: operation of video frames
        for operation in operations:
            output_frames.append(operation(frame))

    print("No frames: " + str(len(input_frames)))
    print("Input Shape:" , input_frames[0].shape)
    print("Output Shape:" , output_frames[0].shape)