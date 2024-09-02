
import cv2


def process_image(image_name, operations):
    input_path = "data/" + image_name
    image = cv2.imread(input_path)
    for operation in operations:
        image = operation(image)
    return image

def draw_on_image(image_name , lines):
    input_path = "data/" + image_name
    output_path = "output/" + image_name
    image = cv2.imread(input_path)

    for line in lines:
        cv2.line(image, (int(line.p1[0]), int(line.p1[1])), (int(line.p2[0]), int(line.p2[1])), (0, 255, 0), 2)

    # Save the processed image
    cv2.imwrite(output_path, image)
    print("Input Image Shape:", image.shape)
    print("Processed image saved to:", output_path)

def apply_func_to_image(image_name, operations):

    input_path = "data/" + image_name
    output_path = "output/" + image_name

    image = cv2.imread(input_path)

    for operation in operations:
        image = operation(image)

    # Save the processed image
    cv2.imwrite(output_path, image)

    print("Input Image Shape:", image.shape)
    print("Processed image saved to:", output_path)