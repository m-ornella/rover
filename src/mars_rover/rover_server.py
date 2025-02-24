from mars_rover import CommunicationServerAbstract
from ..movement import Movement
from ..mars_rover import MarsRover
from typing import Tuple
import socket


class RoverServer:
    def __init__(self, rover: MarsRover, server_implementation: CommunicationServerAbstract):
        self.__rover = rover
        server_implementation.register_on_message_receive_callback(self.on_message_received)
        server_implementation.start()

    def on_message_received(self, message: str) #-> Tuple[int, int, Movement]:
        # if message == "F": self.__rover = self.__rover.move_forward()
        # elif message == 'B': self.__rover = self.__rover.move_backward()
        # elif message == 'L': self.__rover = self.__rover.turn_left()
        # elif message == 'R': self.__rover = self.__rover.turn_right()
        # return self.__rover.position_x, self.__rover.position_y, self.__rover.orientation
        print('[ROVER] Message reçu')
        
    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 8080))
        server.listen(1)

        while True:
            client,addr = server.accept()
            
            client.send('Hello from server'.encode())