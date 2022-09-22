from .vector import Vector
from .point import Point


class Ray:

    def __init__(self, point: Point, vector: Vector) -> None:
        self.point = point
        self.vector = vector

    def get_ang(self):
        return self.vector.get_ang()

    def rotate(self, alpha: float) -> None:
        self.vector.rotate(alpha)

    def displace(self, vec: Vector) -> None:
        self.point.displace(vec)
