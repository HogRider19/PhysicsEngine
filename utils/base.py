import math
from typing import Union
from MathОperators.point import Point
from MathОperators.line import Line
from MathОperators.ray import Ray
from MathОperators.vector import Vector
from Objects.circle import Circle


class RayCast:

    def __init__(self, ray: Ray, object: Union[Line, Circle]) -> None:
        self.ray = ray
        self.object = object

    def get_cross_point(self) -> Union[Point, None]:
        #Вернуть точку пересечения или False
        cross_point = None

        if isinstance(self.object, Line):
            cross_point = self._rc_to_line()
        elif isinstance(self.object, Circle):
            cross_point = self._rc_to_circle()

        return cross_point

    def _rc_to_line(self) -> Union[Point, None]:
        line = self.object
        lineray = MathUtils.ray_to_line(self.ray)

        v = lineray.point2.x - lineray.point1.x
        w = lineray.point2.y - lineray.point1.y

        a,b,c = MathUtils.line_coefficients(line)

        t = (-a * lineray.point1.x - b * lineray.point1.y - c) / (a * v + b * w)

        if t > 0:
            x = lineray.point1.x + v * t
            y = lineray.point1.y + w * t

            return Point(x, y)

        return None 


    def _rc_to_circle(self) -> Union[Point, None]:
        radius = self.object.radius
        dist_line_to_center = MathUtils.distance_point_to_line(self.object.position,
                                                                MathUtils.ray_to_line(self.ray))

        if dist_line_to_center < radius:
            pass

        return None



class MathUtils:

    @staticmethod
    def line_coefficients(line: Line) -> float:
        a = line.point2.y - line.point1.y
        b = line.point1.x - line.point2.x
        c = -line.point1.x  * line.point2.y + line.point1.y * line.point2.x
        return a, b, c

    @staticmethod
    def distance_point_to_line(point: Point, line: Line) -> float:
        a,b,c = MathUtils.line_coefficients(line)
        dist = abs(a*point.x + b*point.y + c) / math.sqrt(a**2 + b**2)
        return dist

    @staticmethod
    def ray_to_line(ray: Ray) -> Line: 
        line = Line(Point(ray.point.x, ray.point.y),
                        Point(ray.vector.x+ray.point.x, ray.vector.y+ray.point.y))
        return line


