from obstacle_interface import IObstacle

class Obstacle(IObstacle):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

