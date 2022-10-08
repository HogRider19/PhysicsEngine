import os,sys
sys.path.append(os.getcwd())

import math
import matplotlib.pyplot as plt
from Objects.circle import Circle
from Objects.rect import Rect
from rendering.pygameR import PygameRender
from simulation.simulation import Simulation
from simulation.space import Space
from MathОperators.point import Point
from MathОperators.vector import Vector


rect1 = Rect(500, 100, position=Point(400, 350), 
                        moment_inertia=1, mas=0.1, veloсity=Vector(0,0))
circle1 = Circle(20, position=Point(700, 200), 
                        moment_inertia=1, mas=0.1, veloсity=Vector(-4, 0))

space = Space(1200, 700, 0, 0.1, 0.1)
simManager = Simulation(space)
simManager.set_objects(
    rect1,
    circle1,
)

pygameRender = PygameRender(simManager, time=None)
pygameRender.run()