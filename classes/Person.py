import math
from classes import (Limb)

class Person:
    def __init__(self,Id):
        self.Id = Id
        self.limbs = []
        self.ratios = []
        self.limbs_MU = 0
        self.limbs_STD = 0
        self.ratios_MU = 0
        self.ratios_STD = 0

    def convert_keypoints(self, keypoints):
        
        self.limbs = []
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

        for connection in connections:
            idx1, idx2 = connection
            x1, y1, conf1 = keypoints[idx1][0], keypoints[idx1][1], keypoints[idx1][2]
            x2, y2, conf2 = keypoints[idx2][0], keypoints[idx2][1], keypoints[idx2][2]
            p1 = [x1, y1]
            p2 = [x2, y2]
            
            if conf1 > 0.5 and conf2 > 0.5: 
                self.limbs.append(Limb(p1, p2))

    def calculate_limb_ratios(self):
        for limb_i in self.limbs:
            for limb_j in self.limbs:
                self.ratios.append(limb_i.calculate_limb_length() / limb_j.calculate_limb_length())


    def calculate_STD(self):      
        sum = 0 
        for ratio in self.ratios:
            sum += (ratio - self.MU)**2

        sum = sum / (len(self.ratios) - 1)
        self.STD = math.sqrt(sum) 

    def show_info(self):
        msg = f"Person ({self.Id}) --> Limbs Mu = {self.limbs_MU}, Limbs STD = {self.limbs_STD} -  Ratios Mu = {self.ratios_MU}, Ratios STD = {self.ratios_STD}"
        print(msg)
        return msg
    
    def show_points(self):
        for limb in self.limbs:
            print(f"limb: {limb.p1} , {limb.p2}" )

