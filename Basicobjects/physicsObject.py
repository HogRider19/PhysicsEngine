from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.point  import Point
from .material import Material
from functools import reduce
import math


dt = 1/100
df = 0.1
dm = 1


class PhysicsObject:

    def __init__(self, position = Point(0,0), material = Material(), 
                                        static = False, mas = 1, moment_inertia = 1,
                                        veloсity = Vector(0,0), ang_veloсity = 0, ang = 0, collect_info=False):
        self.position = position 
        self.material = material
        self.ang = ang
        self.static = static
        self.mas = mas 
        self.moment_inertia = moment_inertia
        self.veloсity = veloсity
        self.ang_veloсity = ang_veloсity
        self.force_list = []
        self.moment_list = []
        self.collision_list = []

        self.collect_info = collect_info
        self.force_info = []
        self.moment_info = []

    def get_momentum(self):
        momentum = Vector(self.veloсity.x, self.veloсity.y)
        momentum.mult(self.mas)
        return momentum

    def add_force(self, force: Vector) -> None:
        self.force_list.append(Vector(force.x * dt, force.y * dt))

    def add_moment(self, moment: float) -> None:
        self.moment_list.append(-moment*dt)

    def add_relative_force(self, force: Vector, point: Point):
        dx = point.x - self.position.x
        dy = point.y - self.position.y
        moment = (dx * force.y + dy * force.x)
        self.add_moment(moment)
        self.add_force(force)

    def _update_force(self):
        res_force = Vector(0,0)
        for force in self.force_list:
            res_force += force
        res_force.mult(1/self.mas)
        self.veloсity += res_force        
        self.force_list = []

    def _update_movent(self):
        res_moment = 0
        for moment in self.moment_list:
            res_moment += moment
        res_moment /= self.moment_inertia
        self.ang_veloсity += res_moment
        self.moment_list = []

    def _update_transform(self):
        self.position.displace(self.veloсity)
        self.ang += self.ang_veloсity

        if abs(self.ang) >= math.pi * 4:
            self.ang = 0

    def _update_joint(self):
        pass
    
    def _collectInfo(self): 
        self.force_info.append(reduce(lambda a,b: a + b, self.force_list, Vector(0, 0)))
        self.moment_info.append(reduce(lambda a,b: a + b, self.moment_list, 0))

    def update(self):

        if self.collect_info:
            self._collectInfo()

        if self.static == False:
            self._update_force()
            self._update_movent()
            self._update_joint()
            self._update_transform()


