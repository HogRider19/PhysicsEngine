import matplotlib.pyplot as plt
from Basicobjects.physicsObject import PhysicsObject
from MathОperators.ray import Ray
from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.line import Line
from utils.base import MathUtils, RayCast
from utils.complex import DistanceBetweenObjects
from Objects.circle import Circle
from Objects.rect import Rect
import time
import pygame as pg

def draw_rect(rect: Rect, sc):
    for line in rect.get_component_lines():
        pg.draw.line(sc, (50,50,255), [line.point1.x, line.point1.y], [line.point2.x, line.point2.y], 3)


#Настройки PyGame
RES = WIDTH, HEIGHT = 1200, 700
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()


rect = Rect(50, 50, position=Point(600, 350))
rect.add_relative_force(Vector(-100,100), Point(500, 300))


#Отрисовка PyGame
while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    rect.update()
    print(rect.ang_veloсity)
    draw_rect(rect, surface)


    pg.display.flip()
    clock.tick(FPS)







