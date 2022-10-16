import os,sys
sys.path.append(os.getcwd())

import math
from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from Objects.circle import Circle
from Objects.rect import Rect
from utils.base import MathUtils, RayCast
from tests.utils import operations_per_second, ReportManager
from utils.complex import DistanceBetweenObjects, CollisionPoint, Interaction



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
        Circle(values(1, 3), position=Point(values(),values())),
        Circle(values(1, 3), position=Point(values(),values()))
    ).get_distance()


@operations_per_second
def rect_component_lines(values):
    rect = Rect(values(1,5), values(1,5), 
            position=Point(values(), values()), ang=values(0, math.pi*2))
    return rect.get_component_lines()


@operations_per_second
def distance_circle_to_rect_test(values):
    return DistanceBetweenObjects(
        Circle(values(1, 3), position=Point(values(),values())),
        Rect(values(1, 5), values(1, 5), position=Point(values(),values()), ang=values(0, math.pi*2))
    ).get_distance()


@operations_per_second
def distance_line_to_line_test(values):
    line1 = Line(Point(values(),values()), Point(values(),values()))
    line2 = Line(Point(values(),values()), Point(values(),values()))
    return MathUtils.distance_line_to_line(line1, line2)


@operations_per_second
def distance_rect_to_rect_test(values):
    return DistanceBetweenObjects(
        Rect(values(1, 5), values(1, 5), position=Point(values(),values()), ang=values(0, math.pi*2)),
        Rect(values(1, 5), values(1, 5), position=Point(values(),values()), ang=values(0, math.pi*2))
    ).get_distance()


@operations_per_second
def cross_point_circle_circle_test(values):
    return CollisionPoint(
        Circle(values(1, 4), position=Point(values(),values())),
        Circle(values(1, 4), position=Point(values(),values())),
    ).get_cross_point()


@operations_per_second
def cross_point_rect_circle_test(values):
    return CollisionPoint(
        Rect(values(1, 4), values(1, 4), position=Point(values(),values())),
        Circle(values(1, 4), position=Point(values(),values())),
    ).get_cross_point()


@operations_per_second
def rect_circle_interaction_test(values):
    interaction = Interaction([
        Rect(values(1, 100), values(1, 100), position=Point(values(),values())),
        Circle(values(1, 40), position=Point(values(),values())),
    ])
    interaction.distribute_interactions()
    return interaction.get_info()

@operations_per_second
def circle_circle_interaction_test(values):
    interaction = Interaction([
        Circle(values(1, 40), position=Point(values(),values())),
        Circle(values(1, 40), position=Point(values(),values())),
    ])
    interaction.distribute_interactions()
    return interaction.get_info()



def report():
    manager = ReportManager()
    
    manager.register(
        line_coefficients_test,
        ray_cast_to_line_test,
        distance_point_to_line_test,
        ray_to_line_test,
        distance_circle_to_circle_test,
        rect_component_lines,
        distance_circle_to_rect_test,
        distance_line_to_line_test,
        distance_rect_to_rect_test,
        cross_point_circle_circle_test,
        cross_point_rect_circle_test,
        rect_circle_interaction_test,
        circle_circle_interaction_test,
    )

    return manager.get_report()


print(report())
