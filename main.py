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


line1 = Line(Point(0,0), Point(0,1))
line2 = Line(Point(1,0), Point(-1,0))

res = MathUtils.distance_line_to_line(line1, line2)

print(res)



