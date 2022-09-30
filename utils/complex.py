import math
from typing import Union
from MathОperators.line import Line
from MathОperators.point import Point
from MathОperators.ray import Ray
from MathОperators.vector import Vector
from Objects.circle import Circle
from Objects.rect import Rect
from utils.base import MathUtils, RayCast
from utils.base import CoordinateSystemRotation


class DistanceBetweenObjects:

    def __init__(self, object1: Union[Rect, Circle], object2: Union[Rect, Circle]) -> None:
        self.object1 = object1
        self.object2 = object2

    def get_distance(self) -> float:
        dist = None

        if isinstance(self.object1, Circle) and  isinstance(self.object2, Circle):
            dist = self._dist_circle_circle()

        elif isinstance(self.object1, Rect) and  isinstance(self.object2, Rect):
            dist = self._dist_rect_rect()

        elif (isinstance(self.object1, Circle) and
                    isinstance(self.object2, Rect)) or (isinstance(self.object2, Circle) and
                        isinstance(self.object1, Rect)):

            if not isinstance(self.object1, Circle):
                # Меняем объксты местами если первый не Circle
                self.object1, self.object2 = self.object2, self.object1

            dist = self._dist_circle_rect()
        
        else:
            raise "Invalid object"

        return dist

    def _dist_circle_circle(self) -> float: 
        radius1 = self.object1.radius
        radius2 = self.object2.radius
        dist = MathUtils.distance_point_to_point(
                self.object1.position, self.object2.position) - (radius1 + radius2)
        dist = 0 if dist < 0 else dist
        return dist

    def _dist_circle_rect(self) -> float: 
        circle = self.object1
        rect = self.object2
        
        dists = []
        for line in rect.get_component_lines():
            dist = MathUtils.distance_point_to_line(circle.position,
                                                     line) - circle.radius
            dist = 0 if dist < 0 else dist
            dists.append(dist)

        return min(dists)

    def _dist_rect_rect(self) -> float: 
        dists = []
        for line1 in self.object1.get_component_lines():
            for line2 in self.object2.get_component_lines():
                dist = MathUtils.distance_line_to_line(line1, line2)
                dist = 0 if dist < 0 else dist
                dists.append(dist)
        
        return min(dists)



class CollisionPoint:
    
    def __init__(self, object1: Union[Rect, Circle], object2: Union[Rect, Circle]) -> None:
        self.object1 = object1
        self.object2 = object2

    def get_cross_point(self) -> float:
        cross_point = None

        if isinstance(self.object1, Circle) and  isinstance(self.object2, Circle):
            cross_point = self._cross_circle_circle()

        elif isinstance(self.object1, Rect) and  isinstance(self.object2, Rect):
            cross_point = self._cross_rect_rect()

        elif (isinstance(self.object1, Circle) and
                    isinstance(self.object2, Rect)) or (isinstance(self.object2, Circle) and
                        isinstance(self.object1, Rect)):

            if not isinstance(self.object1, Circle):
                # Меняем объксты местами если первый не Circle
                self.object1, self.object2 = self.object2, self.object1

            cross_point = self._cross_circle_rect()
        
        else:
            raise "Invalid object"

        return cross_point

    def _cross_circle_circle(self) -> Point: 
        vector12 = Vector(self.object1.position.x - self.object2.position.x,
                             self.object1.position.y  - self.object2.position.y)
        vector12.normalize()
        vector12.mult(self.object1.radius)
        cross_point = self.object1.position.displace_new_point(vector12)
        return cross_point

    def _cross_circle_rect(self) -> Point: 
        """
        1) Получаем точки rect
        2) Поворот системы координат
        3) a = arctg(dy/dx)
        4) a1 = arctg(h/w)
        5) lineNum = 
                3: -a1 < a < a1
                4: a1 < a < pi - a1
                1: pi - a1 < a < pi + a1
                2: pi+a1 < a < 2pi - a1
        6) d = sqrt(dx**2 + dy**2)
        7) d' = dist(Ld and lineNum)
        8) if d <= d':
            return Ld U lineNum
            else:
                None
        """
        rect = self.object1
        circle = self.object2

        lines = rect.get_component_lines()

        rotateManager = CoordinateSystemRotation(ang=rect.ang)

        lines_r = list(map(lambda x: rotateManager.get_transformed_line(x), lines))
        circle_pos_r = rotateManager.get_transformed_point(circle.position)
        rect_pos_r = rotateManager.get_transformed_point(rect.position)

        dx = circle_pos_r.x - rect_pos_r.x
        dy = circle_pos_r.y - rect_pos_r.y

        alpha = math.atan(dy/dx)
        alpha1 = math.atan(rect.height/rect.width)

        lineNum = 0
        if -alpha1 <= alpha <= alpha1:
            lineNum = 2
        elif alpha1 <= alpha <= math.pi - alpha1:
            lineNum = 3
        elif math.pi - alpha1 <= alpha <= math.pi + alpha1:
            lineNum = 0
        elif math.pi + alpha1 <= alpha <= 2*math.pi - alpha1:
            lineNum = 1

        d = math.sqrt(dx**2 + dy**2)
        d1 = MathUtils.distance_point_to_line(rect_pos_r, lines_r[lineNum])

        if d <= d1:
            ray_rect_circle = Ray(rect_pos_r, Vector(dx,dy))
            cross_point_r = RayCast(ray_rect_circle, lines_r[lineNum]).get_cross_point()
            cross_point = rotateManager.get_starting_point(cross_point_r)
            return cross_point

        return None


    def _cross_rect_rect(self) -> Point: 
        pass 