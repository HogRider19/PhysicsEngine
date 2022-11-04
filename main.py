import math
from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from utils.base import MathUtils, RayCast
from utils.complex import DistanceBetweenObjects, CollisionPoint
from Objects.circle import Circle
from Objects.rect import Rect
import matplotlib.pyplot as plt
import time


p = Point(1, 1)
v = Vector(3, 5)
r = Ray(p, v)
l = Line(p, p.displace_new_point(v))

print(p)
print(v)
print(r)
print(l)
