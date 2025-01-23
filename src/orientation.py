class Orientation:
    ORIENTATIONS = ['N', 'E', 'S', 'W']
    MOVEMENTS = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, initial_orientation: str):
        if initial_orientation not in self.ORIENTATIONS:
            raise ValueError(f"Invalid orientation: {initial_orientation}. Must be one of {self.ORIENTATIONS}.")
        self.current_index = self.ORIENTATIONS.index(initial_orientation)

    def move_forward(self, x, y):
        dx, dy = self.MOVEMENTS[self.get_current_orientation()]
        return x + dx, y + dy

    def move_backward(self, x, y):
        dx, dy = self.MOVEMENTS[self.get_current_orientation()]
        return x - dx, y - dy

    def turn_left(self):
        self.current_index = (self.current_index - 1) % len(self.ORIENTATIONS)

    def turn_right(self):
        self.current_index = (self.current_index + 1) % len(self.ORIENTATIONS)

    def get_current_orientation(self):
        return self.ORIENTATIONS[self.current_index]

    def __str__(self):
        return self.get_current_orientation()
