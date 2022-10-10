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


rect1 = Rect(500, 400, position=Point(600, 350), 
                        moment_inertia=1, mas=10.1, veloсity=Vector(0,0))
circle1 = Circle(20, position=Point(1000, 350), 
                        moment_inertia=1, mas=1.1, veloсity=Vector(-3, 0))        
circle2 = Circle(20, position=Point(200, 350), 
                        moment_inertia=1, mas=1.1, veloсity=Vector(3, -0))

space = Space(1200, 700, 0, 0.5, 1.5)
simManager = Simulation(space)
simManager.set_objects(
    rect1,
    circle1,
    circle2,
)

pygameRender = PygameRender(simManager, time=5, collectInfo=True, drawinteraction=False)
pygameRender.run()

info = pygameRender.get_info()

ploter = PloterInfo(info, num_obgect = (0,1,2), drawspace=True)
#ploter.show()
ploter.show_once('xforce')