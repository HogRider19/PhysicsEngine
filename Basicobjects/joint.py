import numpy
from MathОperators.point import *
import numpy as np

class Joint:
    
    def __init__(self,point, object_list, static = True):
        self.point = point
        self.object_list = object_list
        self.statik = static