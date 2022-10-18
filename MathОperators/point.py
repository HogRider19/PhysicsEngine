import math
from .vector import Vector


class Point:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def displace(self, vec: Vector) -> None:
        self.x += vec.x
        self.y += vec.y

    def displace_new_point(self, vec: Vector):
        return Point(
            x = self.x + vec.x,
            y = self.y + vec.y
        )

    def get_displace(self, point) -> float:
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def __eq__(self, other) -> bool:
        return abs(self.x - other.x) <= 0.001 and abs(self.y - other.y) <= 0.001