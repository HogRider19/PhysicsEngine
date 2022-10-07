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
        self._influence_space_update()
        self._replace_object_in_border()
        self._update_objects()

    def _influence_space_update(self) -> None:
        for object in self.objects:
            object.add_force(Vector(0, self.space.gravity))
            object.veloсity.mult(1 - self.space.viscosity/100)
            object.ang_veloсity *= (1 - self.space.viscosity_ang/100)


    def _colision_update(self) -> None:
        for index1, object1 in enumerate(self.objects):
            for index2, object2 in enumerate(self.objects):
                if index1 != index2:
                    collisionPointManager = CollisionPoint(object1, object2)
                    colision_point = collisionPointManager.get_cross_point()

                    if colision_point:

                        momentum = object1.get_momentum() + object2.get_momentum()
                        momentum.mult(0.5)

                        self.objects[index2].add_relative_force(momentum, colision_point)
                        self.objects[index1].add_relative_force(momentum, colision_point)

    def _replace_object_in_border(self):
        for object in self.objects:
            if object.position.x < 0:
                object.position.x = self.space.height - 1
            elif object.position.x > self.space.height:
                object.position.x = 0

            if object.position.y < 0:
                object.position.y = self.space.width - 1
            elif object.position.y > self.space.width:
                object.position.y = 0 

    def _update_objects(self):
        for object in self.objects:
            object.update()
