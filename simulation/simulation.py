from Objects.rect import Rect
from Objects.circle import Circle
from simulation.space import Space
from typing import Union

class Simulation:

    def __init__(self, space: Space) -> None:
        self.space = space
        self.objects = []

    def set_objects(self, *args: Union[Circle, Rect]) -> None:
        for object in args:
            if isinstance(object, (Circle, Rect)):
                self.objects.append(object)
            else:
                raise TypeError("The object must be a Circle or Rect!")

    def update(self) -> None:
        pass
