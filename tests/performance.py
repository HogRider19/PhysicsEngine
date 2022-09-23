from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from utils.base import MathUtils, RayCast
from tests.utils import operations_per_second, ReportManager



@operations_per_second
def line_coefficients_test(values):
    line = Line(Point(values(), values()), Point(values(), values()))
    return MathUtils.line_coefficients(line)


@operations_per_second
def ray_cast_to_line_test(values):
    ray = Ray(Point(values(), values()), Vector(values(), values()))
    line = Line(Point(values(), values()), Point(values(), values()))
    return RayCast(ray, line).get_cross_point()


def get_report():
    manager = ReportManager()
    manager.register(
        line_coefficients_test,
        ray_cast_to_line_test,
    )

    return manager.get_report()
