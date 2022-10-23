import math
import os,sys
sys.path.append(os.getcwd())

from utils.base import RayCast, CoordinateSystemRotation, MathUtils
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


@pytest.mark.parametrize('ang, point, displace, exepted_point',[
                    (math.pi/2, Point(0, 1), Vector(1,0), Point(0,2)),
                    (math.pi/4, Point(1, 1), Vector(math.sqrt(2),0), Point(2,2)),
                    (math.pi, Point(0, 0), Vector(5,0), Point(-5,0)),])
def test_coordinate_system_rotation_point(ang, point, displace, exepted_point):
    rotateManager = CoordinateSystemRotation(ang)
    point_r = rotateManager.get_transformed_point(point)
    point_r.displace(displace)
    res_point = rotateManager.get_starting_point(point_r)
    assert res_point == exepted_point
 

@pytest.mark.parametrize('line, cff', [
                    (Line(Point(1,1),Point(4, 12)), (11, -3,-8)),
                    (Line(Point(-8,1),Point(15,0)), (-1,-23,15)),
                    (Line(Point(0,0),Point(1,0)), (0,-1,0))])
def test_line_coefficients(line, cff):
    res_cff = MathUtils.line_coefficients(line)
    assert cff == res_cff


@pytest.mark.parametrize('point, line, ls, dist', [
                    (Point(10,-2), Line(Point(1,2),Point(3, -8)), False, 8.04),
                    (Point(5,-8), Line(Point(0,0),Point(0, 10)), False, 5),
                    (Point(0, 0), Line(Point(1,0),Point(2, 0)), False, 0),
                    (Point(0, 0), Line(Point(1,0),Point(2, 0)), True, 1),
                    (Point(0, 1), Line(Point(0,0),Point(1, 1)), True, 0.7071),])
def test_distance_point_to_line(point, line, ls, dist):
    d = MathUtils.distance_point_to_line(point, line, ls)
    if d is None or dist is None:
        assert dist == d 
    else: 
        assert abs(dist - d) < 0.01

@pytest.mark.parametrize('line1, line2, dist',[
                    (Line(Point(-1,-1),Point(1, 1)),Line(Point(-1,1),Point(1, -1)), 0),
                    (Line(Point(0,0),Point(0, 1)),Line(Point(1,0),Point(1, 1)), 1),
                    (Line(Point(0,1),Point(1, 0)),Line(Point(1,0),Point(2, 1)), 0),
                    (Line(Point(0,1),Point(1, 0)),Line(Point(2,0),Point(3, 1)), 1),])
def test_distance_line_to_line(line1, line2, dist):
    d = MathUtils.distance_line_to_line(line1, line2)
    assert dist == d
