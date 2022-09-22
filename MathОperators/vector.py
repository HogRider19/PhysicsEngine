import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y)

    def rotate(self, alpha: float) -> None:
        cs = math.cos(alpha)
        sn = math.sin(alpha)    
        rx = self.x * cs - self.y * sn
        ry = self.x * sn + self.y * cs
        self.x,self.y = rx, ry

    def normalize(self) -> None:
        len = self.get_len()
        self.x = self.x/len
        self.y = self.y/len

    def get_len(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_ang(self) -> float:
        return math.atan2(self.y,self.x)

    def mult(self, value: float) -> None:
        self.x,self.y = self.x*value,self.y*value




