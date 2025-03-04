from src.toroidal_planet.obstacle_interface import IObstacle

class Obstacle(IObstacle):
    def __init__(self, __x: int, __y: int, __description: str):
        self.__x = __x
        self.__y = __y
        self.__description = __description
    
    def is_at_position(self, x: int, y: int) -> bool:
        return self.__x == x and self.__y == y

    def __str__(self):
        return f"{self.__description} à ({self.__x}, {self.__y})"
