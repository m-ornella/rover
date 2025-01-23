from abc import ABC, abstractmethod

class IObstacle(ABC):
    @abstractmethod
    def is_at_position(self):
        pass

    @abstractmethod
    def __str__(self):
        pass