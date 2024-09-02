import openpifpaf
import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_predictions(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    predictor = openpifpaf.Predictor()
    predictions, _, _ = predictor.numpy_image(image_rgb)
    return predictions

def draw_keypoints(image):


    predictions = get_predictions(image)
    # The `predictions` variable contains the keypoints and skeleton information
    # You can process or visualize the predictions here

    # Convert back to BGR for OpenCV visualization
    image_with_predictions = image.copy()

    connections = [
        (5, 6),  # left shoulder to right shoulder
        (5, 7),  # left shoulder to left elbow
        (7, 9),  # left elbow to left wrist
        (6, 8),  # right shoulder to right elbow
        (8, 10), # right elbow to right wrist
        (11, 12),# left hip to right hip
        (5, 11), # left shoulder to left hip
        (6, 12), # right shoulder to right hip
        (11, 13),# left hip to left knee
        (13, 15),# left knee to left ankle
        (12, 14),# right hip to right knee
        (14, 16) # right knee to right ankle
    ]

    # Draw predictions on the image
    for pred in predictions:
        keypoints = pred.data  # Access keypoints via the `data` attribute
        for point in keypoints:
            for i in range(0, len(point), 3):
                x, y, confidence = point[i], point[i+1], point[i+2]
                # print(x)
                # print(y)

                if confidence > 0.5:  # You can set a threshold for confidence
                    cv2.circle(image_with_predictions, (int(x), int(y)), 3, (0, 255, 0), -1)

                # Draw the connections (limbs)
        for connection in connections:
            idx1, idx2 = connection
            x1, y1, conf1 = keypoints[idx1][0], keypoints[idx1][1], keypoints[idx1][2]
            x2, y2, conf2 = keypoints[idx2][0], keypoints[idx2][1], keypoints[idx2][2]

            if conf1 > 0.5 and conf2 > 0.5:  # Only draw if both keypoints have high confidence
                cv2.line(image_with_predictions, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    return image_with_predictions    

if __name__ == '__main__':
    img = cv2.imread('C:\\Users\\Mahmoud_Taha\\Downloads\\temp\\fight.jpg')
    img = draw_keypoints(img)

    plt.imshow(cv2.cvtColor(img , cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
