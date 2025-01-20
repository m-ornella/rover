class ToroidalPlanet():
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def wrap_coordinates(self, x: int, y: int):
        x %= self.__width
        y %= self.__height
        return x, y
