from .point import Point
from .vector import Vector
import math


class Line:

    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def get_ang(self):
        v = Vector(self.point1.x - self.point2.x, self.point1.y - self.point2.y)
        return self.v.get_ang()

    def get_guiding_vec(self):
        return Vector(self.point1.x - self.point2.x, self.point1.y - self.point2.y)

    def get_norm_vec(self):
        return self.get_guiding_vec().rotate(math.pi/2)

    def get_len(self):
        return math.sqrt((self.point1.x-self.point2.x)**2 + (self.point1.y-self.point2.y)**2)
