from Objects.rect import Rect
from Objects.circle import Circle
from simulation.space import Space
from MathОperators.line import Line
from MathОperators.point import Point
from MathОperators.vector import Vector
from utils.complex import CollisionPoint
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
        
        self._colision_update()
        self._gravity_update()
        self._update_objects()

    def _gravity_update(self) -> None:
        for object in self.objects:
            object.add_force(Vector(0, self.space.gravity))

    def _colision_update(self) -> None:
        for index1, object1 in enumerate(self.objects):
            for index2, object2 in enumerate(self.objects):
                if index1 != index2:
                    colision_point = CollisionPoint(object1, object2).get_cross_point()

                    if colision_point:
                        object1.add_relative_force(object2.veloсity, colision_point)
                        #object2.add_relative_force(Vector(-object2.veloсity.x, -object2.veloсity.y), colision_point)
                        object2.veloсity = Vector(-object2.veloсity.x, -object2.veloсity.y)

    def _update_objects(self):
        for object in self.objects:
            object.update()
