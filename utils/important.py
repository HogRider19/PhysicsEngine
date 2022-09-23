from typing import Union
from Objects.circle import Circle
from Objects.rect import Rect


class distanceBetweenObjects:

    def __init__(self, object1: Union[Rect, Circle], object2: Union[Rect, Circle]) -> None:
        self.object1 = object1
        self.object2 = object2

    def get_distance(self) -> float:
        pass

    def _dist_circle_circle(self) -> float: 
        pass

    def _dist_circle_rect(self) -> float: 
        pass

    def _dist_rect_rect(self) -> float: 
        pass
