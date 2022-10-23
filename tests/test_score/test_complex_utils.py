import os,sys
sys.path.append(os.getcwd())

from utils.complex import DistanceBetweenObjects
from Objects.circle import Circle
from Objects.rect import Rect
from MathОperators.point import Point
import pytest


@pytest.mark.parametrize('circle1, circle2, dist', [
                            (Circle(1, position=Point(0,0)),Circle(5, position=Point(10,0)),4),
                            (Circle(10, position=Point(0,0)),Circle(10, position=Point(100,100)),121.421),
                            (Circle(10, position=Point(5,5)),Circle(3, position=Point(6,6)),0),
                            (Circle(10, position=Point(0,0)),Circle(10, position=Point(20,0)),0),])
def test_distance_circle_circle(circle1, circle2, dist):
    d = DistanceBetweenObjects(circle1, circle2).get_distance()
    assert abs(dist - d) < 0.01


@pytest.mark.parametrize('circle, rect, dist', [
                            (Circle(1, position=Point(0,0)),Rect(1,1,position=Point(0,0)),0),
                            (Circle(5, position=Point(0,0)),Rect(10,10,position=Point(50,0)),40),])
def test_distance_circle_rect(circle, rect, dist):
    d = DistanceBetweenObjects(circle, rect).get_distance()
    assert abs(dist - d) < 0.01