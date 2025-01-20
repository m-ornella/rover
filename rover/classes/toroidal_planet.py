from ..interfaces.i_planet import IPlanet

class ToroidalPlanet(IPlanet):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wrap_coordinates(self, x, y):
        x %= self.width
        y %= self.height
        return x, y
