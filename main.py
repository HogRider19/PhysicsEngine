from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from utils.base import MathUtils, RayCast
from tests.performance import get_report
from utils.complex import DistanceBetweenObjects
from Objects.circle import Circle
from Objects.rect import Rect


dist = DistanceBetweenObjects(
    Circle(1, position=Point(0,0)),
    Circle(1, position=Point(5,0))
).get_distance()

print(dist)



