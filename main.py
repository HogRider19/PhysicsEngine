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


first_time = time.time()

rect = Rect(50, 50, position=Point(600, 350))
circle = Circle(20, position=Point(600 + 60,350 + 50))

result1 = []
result2 = []

a = 0
while time.time() - first_time < 0.027:

    circle.position.x = math.sin(a)*45 + rect.position.x
    circle.position.y = math.cos(a)*45 + rect.position.y
    a += 0.05
    
    cp = CollisionPoint(rect, circle).get_cross_point()

    if cp:
        result1.append(cp.x - rect.position.x)
        result2.append(-cp.y + rect.position.y)
    else:
        result1.append(0)
        result2.append(0)


# plt.plot(result1)
# plt.plot(result2)
plt.plot(result1, result2)
plt.grid(True)
plt.show()
