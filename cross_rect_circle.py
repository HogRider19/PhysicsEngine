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
import matplotlib.pyplot as plt
from simulation.simulation import Simulation
from simulation.space import Space

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


rect = Rect(500, 100, position=Point(400, 350), moment_inertia=1, mas=0.1, ang=math.pi/2)
circle = Circle(20, position=Point(700, 350), moment_inertia=1, mas=0.1)
circle.veloсity = Vector(-4,0)
rect.veloсity = Vector(0,0)


space = Space(1200, 700, 0, 0, 0)
simManager = Simulation(space)
simManager.set_objects(
    rect,
    circle,
)

rect_ang_vel = []
rect_vel_x = []

circle_force = []

#Отрисовка PyGame
is_sim = True
while is_sim:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            is_sim = False

    draw_rect(rect, surface)
    draw_circle(circle, surface)

    simManager.update()

    pg.display.flip()
    clock.tick(FPS)



plt.plot(rect.memory_force)
plt.grid(True)
plt.show()