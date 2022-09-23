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


rect = Rect(2, 4, position=Point(0,0))

line_list = rect.get_component_lines()

for i in line_list:
    print(f"{i.point1.x}:{i.point1.y}    {i.point2.x}:{i.point2.y}")



