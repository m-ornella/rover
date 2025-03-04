from abc import ABC, abstractmethod

# TODO : utilité avec 1 seule classe concrète ?
class IObstacle(ABC):
    @abstractmethod
    def is_at_position(self):
        pass

    @abstractmethod
    def __str__(self):
        pass