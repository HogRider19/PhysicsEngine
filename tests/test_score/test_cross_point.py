import os,sys
sys.path.append(os.getcwd())

from utils.complex import CollisionPoint
from Objects.circle import Circle
from Objects.rect import Rect
from MathОperators.point import Point
import math
import pytest

def C(x, y, r):
    """Быстрое создание объекта Circle"""
    return Circle(r, position=Point(x,y))

def P(x, y):
    """Быстрое создание объекта Point"""
    return Point(x ,y)


@pytest.mark.parametrize('circle1, circle2, cross_point', [
                                        (C(0, 0, 1), C(2, 0, 1), P(1, 0)),
                                        ])
def test_collision_circle_circle(circle1, circle2, cross_point):
    collisionManager = CollisionPoint(circle1, circle2)
    collisionManager.calculate()
    collisionInfo = collisionManager.get_info()
    assert collisionInfo.get('cross_point') == cross_point