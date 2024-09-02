import numpy as np

class Limb:
    def __init__(self, p1 , p2):
        self.p1 = p1
        self.p2 = p2

    def calculate_limb_length(self):
        return np.sqrt((self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2)
