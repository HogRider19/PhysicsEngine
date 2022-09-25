from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from utils.base import MathUtils, RayCast
from tests.performance import get_report
from utils.complex import DistanceBetweenObjects, CollisionPoint
from Objects.circle import Circle
from Objects.rect import Rect
import matplotlib.pyplot as plt
import time



first_time = time.time()

circle1 = Circle(1, position=Point(0,0))
circle2 = Circle(1, position=Point(10,0))

circle2.add_force(Vector(-0.17, 0))

result = []

while time.time() - first_time < 1:
    dist = DistanceBetweenObjects(circle2, circle1).get_distance()

    #result.append(dist)

    circle1.update()
    circle2.update()

    if dist <= 0:
        p = CollisionPoint(circle2, circle1).get_cross_point()
        result.append(p.x)


plt.plot(result)
plt.grid(True)
plt.show()


