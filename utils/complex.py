from typing import Union
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
        pass
