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


circle1 = Circle(20, position=Point(900, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(0, 0))
circle2 = Circle(20, position=Point(800, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(2, 0))
circle3 = Circle(20, position=Point(700, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(2, 0))
circle4 = Circle(20, position=Point(600, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(2, 0))
circle5 = Circle(20, position=Point(500, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(2, 0))
circle6 = Circle(20, position=Point(400, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(2, 0))
circle7 = Circle(20, position=Point(300, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(2, 0))
circle8 = Circle(20, position=Point(200, 350), 
                        moment_inertia=1, mas=0.05, veloсity=Vector(2, 0))

space = Space(1200, 700, 0, 0.0, 1.5)
simManager = Simulation(space)
simManager.set_objects(
    circle1,
    circle2,
    circle3,
    circle4,
    circle5,
    circle6,
    circle7,
    circle8,
)

pygameRender = PygameRender(simManager, time=8, collectInfo=True, drawinteraction=True)
pygameRender.run()

info = pygameRender.get_info()

ploter = PloterInfo(info, num_obgect = (0,1,2,3,4,5,6,7), drawspace=True)
#loter.show()
ploter.show_once('xforce', 'xvel')