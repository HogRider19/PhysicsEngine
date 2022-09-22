from Basicobjects.physicsObject import PhysicsObject


class Rect(PhysicsObject):

    def __init__(self, height: float, width: float, *args, **kwargs):
        self.height = height
        self.width = width
        super().__init__(*args, **kwargs)