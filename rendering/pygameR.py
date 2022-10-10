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

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self, simManager: Simulation, time: float, width=1200,
                    height=700, collectInfo=False, drawinteraction=False) -> None:
        self.simManager = simManager
        self.time = time
        self.width = width
        self.height = height
        self.collectInfo = collectInfo
        self.drawinteraction = drawinteraction
        self.info = []
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
            if self.drawinteraction:
                self._draw_interaction()

            if self.collectInfo:
                self._collect_info()

            pg.display.flip()
            self.clock.tick(self.FPS)

    def get_info(self) -> list:
        return self.info

    def _prepare(self) -> None:
        pg.init()
        self.scr = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.is_sim = True
        
        if self.collectInfo:
            for i in range(len(self.simManager.get_objects())):
                self.simManager.objects[i].collect_info = True
                self.info.append({
                    'xpos': [],
                    'ypos': [],
                    'ang':  [],
                    'xvel': [],
                    'yvel': [],
                    'angvel': [],
                    'xforce': [],
                    'yforce': [],
                    'moment': [],
                })

    def _collect_info(self) -> None:
        for index, object in enumerate(self.simManager.get_objects()):
            own_info = self.info[index]
            own_info['xpos'].append(object.position.x)
            own_info['ypos'].append(object.position.y)
            own_info['xvel'].append(object.veloсity.x)
            own_info['yvel'].append(object.veloсity.y)   
            own_info['xforce'] = list(map(lambda a:a.x, object.force_info))
            own_info['yforce'] = list(map(lambda a:a.y, object.force_info))  
            own_info['moment'] = object.moment_info  
            own_info['ang'].append(object.ang) 
            own_info['angvel'].append(object.ang_veloсity)     

    def _draw_obgects(self) -> None:
        for object in self.simManager.get_objects():
            if isinstance(object, Circle):
                self._draw_circle(object)
            elif isinstance(object, Rect):
                self._draw_rect(object)
            else:
                raise TypeError("The object must be a Circle or Rect!")

    def _draw_interaction(self) -> None:
        interinfo = self.simManager.get_interaction_info()

        if interinfo:
            cp = interinfo.get('cross_point')
            fv = interinfo.get('force_vector')
            fv.mult(4)
            
            pg.draw.circle(self.scr, (255,20,20), 
                        (cp.x, cp.y), 10)

            self._draw_line(Line(cp, cp.displace_new_point(fv)), color=(255,255,255))

    def _draw_rect(self, rect, color=(50,50,255)) -> None:
        for line in rect.get_component_lines():
            pg.draw.line(self.scr, color, [line.point1.x, line.point1.y], [line.point2.x, line.point2.y], 3)

    def _draw_circle(self, circle: Circle, color=(225, 225, 0)) -> None:
        pg.draw.circle(self.scr, color, 
                    (circle.position.x, circle.position.y), circle.radius)

    def _draw_line(self, line: Line, color=(255,50,50)) -> None:
        pg.draw.line(self.scr, color, [line.point1.x, line.point1.y], [line.point2.x, line.point2.y], 3)