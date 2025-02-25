from mars_rover import CommunicationServerAbstract
from ..mars_rover import MarsRover


class RoverServer:
    def __init__(self, rover: MarsRover, server_implementation: CommunicationServerAbstract):
        self.__rover = rover
        server_implementation.register_on_message_receive_callback(self.on_message_received)
        server_implementation.start()

    def on_message_received(self, message: str):
        if message == "A": self.__rover = self.__rover.move_forward()
        return self.__rover.position_x, self.__rover.position_y, self.__rover.orientation
        pass