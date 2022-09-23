from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from Objects.circle import Circle
from Objects.rect import Rect
from utils.base import MathUtils, RayCast
from tests.utils import operations_per_second, ReportManager
from utils.complex import DistanceBetweenObjects



@operations_per_second
def line_coefficients_test(values):
    line = Line(Point(values(), values()), Point(values(), values()))
    return MathUtils.line_coefficients(line)


@operations_per_second
def ray_cast_to_line_test(values):
    ray = Ray(Point(values(), values()), Vector(values(), values()))
    line = Line(Point(values(), values()), Point(values(), values()))
    return RayCast(ray, line).get_cross_point()


@operations_per_second
def distance_point_to_line_test(values):
    point = Point(values(), values())
    line = Line(Point(values(), values()), Point(values(), values()))
    return MathUtils.distance_point_to_line(point, line)


@operations_per_second
def ray_to_line_test(values):
    ray = Ray(Point(values(), values()), Vector(values(), values()))
    return MathUtils.ray_to_line(ray)


@operations_per_second
def distance_circle_to_circle_test(values):
    return DistanceBetweenObjects(
        Circle(values(), position=Point(values(),values())),
        Circle(values(), position=Point(values(),values()))
    ).get_distance()


def get_report():
    manager = ReportManager()
    
    manager.register(
        line_coefficients_test,
        ray_cast_to_line_test,
        distance_point_to_line_test,
        ray_to_line_test,
        distance_circle_to_circle_test,
    )

    return manager.get_report()
