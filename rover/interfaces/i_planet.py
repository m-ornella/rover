from abc import ABC, abstractmethod

class IPlanet(ABC):
    @abstractmethod
    def wrap_coordinates(self, x, y):
        pass
