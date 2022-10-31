import os,sys
sys.path.append(os.getcwd())

from utils.complex import DistanceBetweenObjects
from Objects.circle import Circle
from Objects.rect import Rect
from MathОperators.point import Point
from MathОperators.line import Line
from MathОperators.vector import Vector
import math
import pytest

def L(x1, y1, x2, y2):
    """Короткое создание оъекта Line"""
    return Line(Point(x1, y1), Point(x2, y2))

@pytest.mark.parametrize('rect, points', [
                    (Rect(10,10, position=Point(0,0), ang=0),[Point(-5,5),Point(-5,-5),Point(5,-5),Point(5,5)]),
                    (Rect(10,10, position=Point(0,0), ang=math.pi/2),[Point(-5,-5),Point(5,-5),Point(5,5),Point(-5,5)]),
                    (Rect(10,10, position=Point(0,0), ang=math.pi/4),[Point(-7.071,0),Point(0,-7.071),Point(7.071,0),Point(0,7.071)]),
                    (Rect(10,10, position=Point(1,1), ang=math.pi/4),[Point(-6.071,1),Point(1,-6.071),Point(8.071,1),Point(1,8.071)]),])
def test_component_points(rect, points):
    ps = rect.get_component_points()
    for index, point in enumerate(points):
        assert abs(point.x - ps[index].x) < 0.01 and abs(point.y - ps[index].y) < 0.01

@pytest.mark.parametrize('rect, lines', [
        (Rect(10,10, position=Point(0,0), ang=0),[L(-5,5,-5,-5),L(-5,-5,5,-5),L(5,-5,5,5),L(5,5,-5,5)]),
        (Rect(10,10, position=Point(10,10), ang=0),[L(5,15,5,5),L(5,5,15,5),L(15,5,15,15),L(15,15,5,15)]),
        (Rect(10,10, position=Point(0,0), ang=math.pi/4),[L(-7.071,0,0,-7.071),L(0,-7.071,7.071,0),L(7.071,0,0,7.071),L(0,7.071,-7.071,0)]),])
def test_component_lines(rect, lines):
    ls = rect.get_component_lines()
    for index, line in enumerate(ls):
        assert line.point1 == lines[index].point1 and line.point2 == lines[index].point2


@pytest.mark.parametrize('vec, ang, res_vec', [
                                (Vector(1,0),math.pi,Vector(-1,0)),
                                (Vector(1,0),math.pi/2,Vector(0,1)),
                                (Vector(1,0),math.pi/4,Vector(1,1)),])
def test_vector_rotate(vec, ang, res_vec):
    vec.rotate(ang)
    assert vec == res_vec

