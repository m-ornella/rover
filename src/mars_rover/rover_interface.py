from abc import ABC, abstractmethod

class IRover(ABC):
    @abstractmethod
    def move_forward(self):
        pass

    @abstractmethod
    def move_backward(self):
        pass

    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass

    @abstractmethod
    def get_state(self):
        pass
