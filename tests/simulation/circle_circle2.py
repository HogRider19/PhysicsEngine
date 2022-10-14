import os,sys
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
from Basicobjects.material import Material


circle1 = Circle(80, position=Point(700, 200), 
                        moment_inertia=1, mas=1.5, veloсity=Vector(-1, 0))
circle2 = Circle(80, position=Point(500, 200), 
                        moment_inertia=1, mas=1.5, veloсity=Vector(1, -0))
circle3 = Circle(80, position=Point(700, 500), 
                        moment_inertia=1, mas=1.5, veloсity=Vector(-1, 0), material=Material(1,1))
circle4 = Circle(80, position=Point(500, 500), 
                        moment_inertia=1, mas=1.5, veloсity=Vector(1, -0), material=Material(1,1))

space = Space(1200, 700, 0, 0.0, 1.5)
simManager = Simulation(space)
simManager.set_objects(
    circle1,
    circle2,
    circle3,
    circle4,
)

pygameRender = PygameRender(simManager, time=4, collectInfo=True, drawinteraction=True)
pygameRender.run()

info = pygameRender.get_info()

ploter = PloterInfo(info, num_obgect = (0,1,2,3), drawspace=True)
#ploter.show()
ploter.show_once('xforce', 'xvel')