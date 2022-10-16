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


rect1 = Rect(500, 200, position=Point(700, 350), 
                        moment_inertia=1, mas=10.1, veloсity=Vector(0,0))
circle1 = Circle(20, position=Point(400, 200), 
                        moment_inertia=1, mas=1.1, veloсity=Vector(3, 0), material=Material(1,1))

space = Space(1200, 700, 0, 0.5, 0.5)
simManager = Simulation(space)
simManager.set_objects(
    rect1,
    circle1,
)

pygameRender = PygameRender(simManager, time=4, collectInfo=True, drawinteraction=False)
pygameRender.run()

info = pygameRender.get_info()

ploter = PloterInfo(info, num_obgect = (0,1), drawspace=True)
ploter.show()
#ploter.show_once('moment', 'ang')


