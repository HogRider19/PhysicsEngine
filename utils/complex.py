from typing import Union
from MathОperators.point import Point
from MathОperators.vector import Vector
from Objects.circle import Circle
from Objects.rect import Rect
from utils.base import MathUtils


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
        pass

    def _cross_rect_rect(self) -> Point: 
        pass 