import math
from turtle import back, position
import matplotlib.pyplot as plt
from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from utils.base import MathUtils, RayCast
from utils.complex import DistanceBetweenObjects, CollisionPoint
from Objects.circle import Circle
from Objects.rect import Rect
import time
import pygame as pg

def draw_rect(rect: Rect, sc):
    for line in rect.get_component_lines():
        pg.draw.line(sc, (50,50,255), [line.point1.x, line.point1.y], [line.point2.x, line.point2.y], 3)

def draw_circle(circle: Circle, sc):
    pg.draw.circle(sc, (225, 225, 0), 
                   (circle.position.x, circle.position.y), circle.radius)

def draw_info(info, sc):
    if info['cross_point']:
        cp = info['cross_point']
        pg.draw.circle(sc, (255, 0, 0), 
                    (cp.x, cp.y), 5)

    pg.draw.line(sc, (50,50,255), [info['line_c_r'].point1.x, info['line_c_r'].point1.y], [info['line_c_r'].point2.x, info['line_c_r'].point2.y], 3)

    f1 = pg.font.Font(None, 22)
    text1 = f1.render(f"alpha: {info['alpha']/3.14/2*350}", True,(180, 0, 0))
    text2 = f1.render(f"alpha1: {info['alpha1']/3.14/2*350}", True,(180, 0, 0))
    text3 = f1.render(f"d: {info['d']}", True,(180, 0, 0))
    text4 = f1.render(f"d1: {info['d1']}", True,(180, 0, 0))
    text5 = f1.render(f"lineNum: {info['lineNum']}", True,(180, 0, 0))

    sc.blit(text1, (10, 50))
    sc.blit(text2, (10, 70))
    sc.blit(text3, (10, 90))
    sc.blit(text4, (10, 110))
    sc.blit(text5, (10, 130))


#Настройки PyGame
RES = WIDTH, HEIGHT = 1200, 700
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()


rect = Rect(50, 50, position=Point(600, 350))
circle = Circle(20, position=Point(600 + 50,350 + 50))

info = CollisionPoint(rect, circle).get_cross_point()

a = 0.1
#Отрисовка PyGame
while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    draw_rect(rect, surface)
    draw_circle(circle, surface)

    circle.position.x = math.sin(a)*50 + rect.position.x
    circle.position.y = math.cos(a)*50 + rect.position.y
    a+=0.05
    info = CollisionPoint(rect, circle).get_cross_point()

    pg.display.flip()
    clock.tick(FPS)