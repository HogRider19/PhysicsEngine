from Basicobjects.physicsObject import PhysicsObject
from utils.moment import circle_moment


class Circle(PhysicsObject):
    
    def __init__(self, radius: float, *args, **kwargs):
        self.radius = radius
        super().__init__(*args, **kwargs)