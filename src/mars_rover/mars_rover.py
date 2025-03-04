from src.mars_rover.rover_interface import IRover
from src.toroidal_planet.toroidal_planet import ToroidalPlanet
from src.mars_rover.movement import Movement

# TODO : nommage à revoir
class MarsRover(IRover):
    # TODO : orientation typage dangereux
    def __init__(self, x: int, y: int, orientation: str, planet: ToroidalPlanet):
        self.x = x
        self.y = y
        self.orientation_handler = Movement(orientation)
        self.planet = planet

    def _try_move(self, new_x, new_y):
        if self.planet.is_obstacle(new_x, new_y):
            print(f"!!! Rover bloqué aux coordonnées: ({self.x}, {self.y}) !!!") # TODO : mélange des genres entre log et logique
        else:
            self.x, self.y = new_x, new_y

    def move_forward(self):
        new_x, new_y = self.orientation_handler.move_forward(self.x, self.y)
        new_x, new_y = self.planet.wrap_coordinates(new_x, new_y)
        self._try_move(new_x, new_y)

    def move_backward(self):
        new_x, new_y = self.orientation_handler.move_backward(self.x, self.y)
        new_x, new_y = self.planet.wrap_coordinates(new_x, new_y)
        self._try_move(new_x, new_y)

    def turn_left(self):
        self.orientation_handler.turn_left()

    def turn_right(self):
        self.orientation_handler.turn_right()

    def get_state(self):
        return f"Position: ({self.x}, {self.y}), Orientation: {self.orientation_handler}"