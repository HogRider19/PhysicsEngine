from Basicobjects.physicsObject import PhysicsObject
from MathОperators.line import Line
from MathОperators.point import Point
from MathОperators.vector import Vector
from utils.base import CoordinateSystemRotation


class Rect(PhysicsObject):

    def __init__(self, height: float, width: float, *args, **kwargs):
        self.height = height
        self.width = width
        super().__init__(*args, **kwargs)

    def get_component_lines(self) -> list:
        """Возвращает список составных линий"""
        rotateManager = CoordinateSystemRotation(ang = self.ang)
        center_r = rotateManager.get_transformed_point(self.position)

        p1_r = center_r.displace_new_point(Vector(-self.width/2, self.height/2))
        p2_r = p1_r.displace_new_point(Vector(0, -self.height))
        p3_r = p2_r.displace_new_point(Vector(self.width, 0))
        p4_r = p3_r.displace_new_point(Vector(0, self.height))

        p1 = rotateManager.get_starting_point(p1_r)
        p2 = rotateManager.get_starting_point(p2_r)
        p3 = rotateManager.get_starting_point(p3_r)
        p4 = rotateManager.get_starting_point(p4_r)

        line1 = Line(p1, p2)
        line2 = Line(p2, p3)
        line3 = Line(p3, p4)
        line4 = Line(p4, p1)

        return [line1, line2, line3, line4]
