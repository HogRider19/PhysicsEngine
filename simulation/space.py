

class Space:

    def __init__(self, height: float, width: float, gravity = 0, viscosity = 0, viscosity_ang = 0) -> None:
        self.height = height
        self.width = width
        self.gravity = gravity
        self.viscosity = viscosity
        self.viscosity_ang = viscosity_ang