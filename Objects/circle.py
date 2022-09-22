from Basicobjects.physicsObject import PhysicsObject


class Circle(PhysicsObject):
    
    def __init__(self, radius: float, *args, **kwargs):
        self.radius = radius
        super().__init__(*args, **kwargs)