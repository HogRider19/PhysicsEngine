from MathОperators.point import Point
from MathОperators.vector import Vector
from MathОperators.point  import Point
from .material import Material
import math


class PhysicsObject:

    def __init__(self, position = Point(0,0), material = Material(), 
                                        static = False, mas = 1, moment_inertia = 1,
                                        veloсity = Vector(0,0), ang_veloсity = 0, ang = 0):
        self.position = position 
        self.material = material
        self.ang = ang
        self.material = Material()
        self.static = static
        self.mas = mas 
        self.moment_inertia = moment_inertia
        self.veloсity = veloсity
        self.ang_veloсity = ang_veloсity
        self.force_list = []
        self.moment_list = []
        self.collision_list = []

    def add_force(self, force: Vector) -> None:
        self.force_list.append(force)

    def add_moment(self, moment: float) -> None:
        self.moment_list.append(moment)

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

    def update(self):
        if self.static == False:
            self._update_force()
            self._update_movent()
            self._update_joint()
            self._update_transform()

