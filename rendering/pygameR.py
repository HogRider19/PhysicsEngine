import sys,os
sys.path.append(os.getcwd())

from simulation.simulation import Simulation
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

class PygameRender:

    def __init__(self, simManager: Simulation, time: float, width=1200, height=700) -> None:
        self.simManager = simManager
        self.time = time
        self.width = width
        self.height = height
        self.FPS = 60
        self.is_sim = True
        self.src = None
        self.clock = None

        self._prepare()

    def run(self) -> None:
        
        back_time = time.time()
        while self.is_sim:
            self.scr.fill(pg.Color('black'))

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    self.is_sim = False
            
            if self.time:
                if time.time() - back_time > self.time:
                    self.is_sim = False

            self.simManager.update()
            self._draw_obgects()

            pg.display.flip()
            self.clock.tick(self.FPS)

    def _prepare(self) -> None:
        pg.init()
        self.scr = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.is_sim = True

    def _draw_obgects(self) -> None:
        for object in self.simManager.get_objects():
            if isinstance(object, Circle):
                self._draw_circle(object)
            elif isinstance(object, Rect):
                self._draw_rect(object)
            else:
                raise TypeError("The object must be a Circle or Rect!")


    def _draw_rect(self, rect) -> None:
        for line in rect.get_component_lines():
            pg.draw.line(self.scr, (50,50,255), [line.point1.x, line.point1.y], [line.point2.x, line.point2.y], 3)

    def _draw_circle(self, circle: Circle) -> None:
        pg.draw.circle(self.scr, (225, 225, 0), 
                    (circle.position.x, circle.position.y), circle.radius)

    