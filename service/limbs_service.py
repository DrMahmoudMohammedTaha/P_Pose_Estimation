import numpy as np
import cv2
import openpifpaf
import math 
import statistics
from classes import (Person)
from classes import (Limb)

def convert_keypoints_to_persons(keypoints_all, seed = 0):

    people = []  

    for keypoints in keypoints_all:
        p = Person(seed)
        seed = seed + 1 
        p.convert_keypoints(keypoints.data)
        p.calculate_limb_ratios()
        if(p.limbs):
            p.limbs_MU = statistics.mean([limb.calculate_limb_length() for limb in p.limbs])
            p.ratios_MU = statistics.mean(p.ratios)
            p.limbs_STD = statistics.stdev([limb.calculate_limb_length() for limb in p.limbs])
            p.ratios_STD = statistics.stdev(p.ratios)
            p.show_info()
        people.append(p)
        
    return people


def search_target(target, people):
    
    print(people[0].ratios_MU)
    people = sorted(people, key = lambda person: person.ratios_MU - target.ratios_MU)
    people[0].show_info()
    people[0].show_points()
    return people[0]
        
