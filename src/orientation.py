class Orientation:
    ORIENTATIONS = ['N', 'E', 'S', 'W']

    def __init__(self, initial_orientation: str):
        if initial_orientation not in self.ORIENTATIONS:
            raise ValueError(f"Invalid orientation: {initial_orientation}. Must be one of {self.ORIENTATIONS}.")
        self.current_index = self.ORIENTATIONS.index(initial_orientation)

    def move_forward(self, x: int, y: int) -> (int, int):
        if self.ORIENTATIONS[self.current_index] == 'N':  
            return x, y + 1
        elif self.ORIENTATIONS[self.current_index] == 'E':  
            return x + 1, y
        elif self.ORIENTATIONS[self.current_index] == 'S':  
            return x, y - 1
        elif self.ORIENTATIONS[self.current_index] == 'W':  
            return x - 1, y

    def move_backward(self, x: int, y: int) -> (int, int):
        if self.ORIENTATIONS[self.current_index] == 'N':
            return x, y - 1
        elif self.ORIENTATIONS[self.current_index] == 'E':  
            return x - 1, y
        elif self.ORIENTATIONS[self.current_index] == 'S':  
            return x, y + 1
        elif self.ORIENTATIONS[self.current_index] == 'W':  
            return x + 1, y

    def turn_left(self):
        self.current_index = (self.current_index - 1) % len(self.ORIENTATIONS)

    def turn_right(self):
        self.current_index = (self.current_index + 1) % len(self.ORIENTATIONS)
