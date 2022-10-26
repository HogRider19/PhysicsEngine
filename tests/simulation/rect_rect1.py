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


rect1 = Rect(500, 200, position=Point(900, 350), 
                        moment_inertia=1, mas=1.1, veloсity=Vector(0,0))
rect2 = Rect(400, 100, position=Point(500, 400), 
                        moment_inertia=1, mas=20.1, veloсity=Vector(2, 0), ang_veloсity=0.01, ang=3.14/2)

space = Space(1200, 700, 0, 0.5, 0.5)
simManager = Simulation(space)
simManager.set_objects(
    rect1,
    rect2,
)

pygameRender = PygameRender(simManager, time=5, collectInfo=True, drawinteraction=True)
pygameRender.run()

info = pygameRender.get_info()

ploter = PloterInfo(info, num_obgect = (0,1), drawspace=True)
#ploter.show()
ploter.show_once('xforce', 'xvel')