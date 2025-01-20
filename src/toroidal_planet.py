class ToroidalPlanet():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def wrap_coordinates(self, x, y):
        x %= self.__width
        y %= self.__height
        return x, y
