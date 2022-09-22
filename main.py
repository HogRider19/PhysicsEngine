from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from utils.base import MathUtils, RayCast
from tests.decorators import operations_per_second


@operations_per_second
def test(values):
    ray = Ray(Point(values(), values()), Vector(values(), values()))
    line = Line(Point(values(), values()),Point(values(), values()))
    return RayCast(ray, line).get_cross_point()


print(test())
