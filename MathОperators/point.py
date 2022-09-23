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