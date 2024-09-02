from utils import (read_video, 
                   save_video,
                   apply_func_to_video,
                   apply_func_to_image,
                   process_image,
                   draw_on_image
                   )
from service import(draw_keypoints,get_predictions,convert_keypoints_to_persons, search_target)


def search_person_task(source_image , search_image):
    preds = process_image(source_image,[get_predictions])
    source = convert_keypoints_to_persons(preds)
    preds = process_image(search_image,[get_predictions])
    people = convert_keypoints_to_persons(preds)
    selected = search_target(source[0], people)
    draw_on_image(search_image,selected.limbs)

if __name__ == '__main__':

    # apply_func_to_video("test-1" , [draw_keypoints])
    source_img = "mo.jpg"
    search_images = ["mo-3.jpg", "mo-5.jpg"]
    
    for img in search_images:
        search_person_task(source_img,img)




