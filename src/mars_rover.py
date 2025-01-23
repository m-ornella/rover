from .rover_interface import IRover
from .toroidal_planet import ToroidalPlanet
from .orientation import Orientation

class MarsRover(IRover):
    def __init__(self, x: int, y: int, orientation: str, planet: ToroidalPlanet):
        self.x = x
        self.y = y
        self.orientation_handler = Orientation(orientation)
        self.planet = planet

    def move_forward(self):
        self.x, self.y = self.orientation_handler.move_forward(self.x, self.y)
        self.x, self.y = self.planet.wrap_coordinates(self.x, self.y)

    def move_backward(self):
        self.x, self.y = self.orientation_handler.move_backward(self.x, self.y)
        self.x, self.y = self.planet.wrap_coordinates(self.x, self.y)

    def turn_left(self):
        self.orientation_handler.turn_left()

    def turn_right(self):
        self.orientation_handler.turn_right()

    def get_state(self):
        return f"Position: ({self.x}, {self.y}), Orientation: {self.orientation_handler}"
