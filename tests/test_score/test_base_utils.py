import os,sys
sys.path.append(os.getcwd())

from utils.base import RayCast
from MathОperators.point import Point
from MathОperators.line import Line
from MathОperators.ray import Ray
from MathОperators.vector import Vector
from Objects.circle import Circle
import pytest


@pytest.mark.parametrize('ray, line, cross_point',[
                    (Ray(Point(0,0),Vector(0,1)), Line(Point(1,1),Point(-1,1)), Point(0,1)),
                    (Ray(Point(0,1),Vector(0,-1)), Line(Point(1,0),Point(-1,0)), Point(0,0)),
                    (Ray(Point(0,-4),Vector(1.333,4)), Line(Point(0,2),Point(2,-4)), Point(1,-1)),
                    (Ray(Point(0,0),Vector(0,1)), Line(Point(-5,-5),Point(5,-5)), None),
                    (Ray(Point(-1,-1),Vector(-1,-1)), Line(Point(0,0),Point(10,10)), None),])
def test_ray_cast(ray, line, cross_point):
    cp = RayCast(ray, line).get_cross_point()
    assert cp == cross_point 