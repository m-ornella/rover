class Orientation:
    ORIENTATIONS = ['N', 'E', 'S', 'W']

    def __init__(self, initial_orientation: str):
        if initial_orientation not in self.ORIENTATIONS:
            raise ValueError(f"Invalid orientation: {initial_orientation}. Must be one of {self.ORIENTATIONS}.")
        self.current_index = self.ORIENTATIONS.index(initial_orientation)

    def move_forward(self):
        if self == 'N':
           self.y += 1
        elif self == 'S':
            self.y -= 1
        elif self == 'E':
            self.x += 1
        elif self == 'W':
            self.x -= 1
        self.x, self.y = self.planet.wrap_coordinates(self.x, self.y)

    def move_backward(self):
        if self == 'N':
            self.y -= 1
        elif self == 'S':
            self.y += 1
        elif self == 'E':
            self.x -= 1
        elif self == 'W':
            self.x += 1
        self.x, self.y = self.planet.wrap_coordinates(self.x, self.y)
    def turn_left(self):
        """Tourne de 90° à gauche (anti-horaire)."""
        self.current_index = (self.current_index - 1) % len(self.ORIENTATIONS)

    def turn_right(self):
        """Tourne de 90° à droite (horaire)."""
        self.current_index = (self.current_index + 1) % len(self.ORIENTATIONS)
