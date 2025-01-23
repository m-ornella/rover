class ToroidalPlanet():
    def __init__(self, width: int, height: int, obstacles=None):
        self.__width = width
        self.__height = height
        self.obstacles = obstacles if obstacles else set()

    def wrap_coordinates(self, x: int, y: int):
        x %= self.__width
        y %= self.__height
        return x, y
    
    def is_obstacle(self, x:int, y: int):
        return (x,y) in self.obstacles
    
    
