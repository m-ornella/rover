from abc import ABC, abstractmethod

class IObstacle(ABC):
    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def __str__(self):
        pass