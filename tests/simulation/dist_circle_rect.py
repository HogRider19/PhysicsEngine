import os,sys
from re import L
sys.path.append(os.getcwd())

import math
import matplotlib.pyplot as plt
from rendering.matplotR import PloterInfo
from Objects.circle import Circle
from Objects.rect import Rect
from rendering.pygameR import PygameRender
from simulation.simulation import Simulation
from simulation.space import Space
from MathОperators.point import Point
from MathОperators.vector import Vector
from utils.complex import DistanceBetweenObjects

def post_action(simManager: Simulation, context: dict):
    if 'a' not in context:
        objects = simManager.get_objects()
        rect = objects[0]
        circle = objects[1]
        context.update({
            'a': 0,
            'rect': rect,
            'circle': circle,
            'dist': []
        })

    a = context['a']
    circle = context['circle']
    rect = context['rect']

    circle.position = Point(
        math.cos(a)*200 + 600,
        math.sin(a)*200 + 350,
    )
    context['a'] -= 0.03
    context['dist'].append(DistanceBetweenObjects(circle, rect).get_distance())
    

rect1 = Rect(100, 100, position=Point(600, 350), 
                        moment_inertia=1, mas=20.1, veloсity=Vector(0,0), ang_veloсity=0, ang=0)
circle1 = Circle(20, position=Point(800, 350), 
                        moment_inertia=1, mas=2.1, veloсity=Vector(-4, 0))     
circle1 = Rect(100, 100, position=Point(800, 350), 
                        moment_inertia=1, mas=20.1, veloсity=Vector(0,0), ang_veloсity=+0, ang=math.pi/4) 


space = Space(1200, 700, 0, 0.5, 1.5)
simManager = Simulation(space)
simManager.set_objects(
    rect1,
    circle1,
)

pygameRender = PygameRender(simManager, time=5, collectInfo=True, drawinteraction=True)
pygameRender.set_post_action(post_action)
pygameRender.run()

info = pygameRender.get_info()


dist = pygameRender.post_action_context['dist']

plt.plot(dist)
plt.fill_between(list(range(len(dist))),dist, [0]*len(dist), color='deepskyblue')
plt.grid(True)
plt.show()




