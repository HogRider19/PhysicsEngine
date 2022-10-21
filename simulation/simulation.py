from Objects.rect import Rect
from Objects.circle import Circle
from simulation.space import Space
from MathОperators.line import Line
from MathОperators.point import Point
from MathОperators.vector import Vector
from utils.complex import CollisionPoint, Interaction
from typing import Union


class Simulation:

    def __init__(self, space: Space) -> None:
        self.space = space
        self.objects = []
        self.interactionManager = Interaction()

    def set_objects(self, *args: Union[Circle, Rect]) -> None:
        for object in args:
            if isinstance(object, (Circle, Rect)):
                self.interactionManager.add_object(object)
                self.objects.append(object)
            else:
                raise TypeError("The object must be a Circle or Rect!")

    def get_objects(self) -> list:
        return self.objects

    def get_interaction_info(self) -> dict:
        return self.interactionManager.get_info()

    def update(self) -> None:

        self.interactionManager.distribute_interactions()

        for object in self.objects:
            self._influence_space_update(object)
            self._replace_object_in_border(object)
            object.update()

    def _influence_space_update(self, object) -> None:
        if self.space.gravity:
            object.add_force(Vector(0, self.space.gravity))
        object.veloсity.mult(1 - self.space.viscosity/100)
        object.ang_veloсity *= (1 - self.space.viscosity_ang/100)

    def _replace_object_in_border(self, object):
        if object.position.x < 0:
            object.position.x = self.space.height - 1
        elif object.position.x > self.space.height:
            object.position.x = 0

        if object.position.y < 0:
            object.position.y = self.space.width - 1
        elif object.position.y > self.space.width:
            object.position.y = 0 
