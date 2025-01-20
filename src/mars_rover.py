from .rover_interface import IRover

class MarsRover(IRover):
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, x, y, direction, planet):
        self.x = x
        self.y = y
        self.direction = direction
        self.planet = planet

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        self.x, self.y = self.planet.wrap_coordinates(self.x, self.y)

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        self.x, self.y = self.planet.wrap_coordinates(self.x, self.y)

    def turn_left(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) - 1) % 4]

    def turn_right(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) + 1) % 4]

    def get_state(self):
        return f"Position: ({self.x}, {self.y}), Direction: {self.direction}"
