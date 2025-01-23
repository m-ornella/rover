from abc import ABC, abstractmethod

class IObstacle(ABC):
    @abstractmethod
    def get_state(self):
        pass