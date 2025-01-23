from .obstacle_interface import IObstacle

class Obstacle(IObstacle):
    def __init__(self, __x: int, __y: int, __description: str):
        self.__x = __x
        self.__y = __y
        self.__description = __description

    def get_position(self):
        return self.__x, self.__y
    
    def __str__(self):
        return f"{self.__description} at ({self.__x}, {self.__y})"
