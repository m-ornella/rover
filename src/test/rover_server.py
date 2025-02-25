# rover_server.py
from socket_communication import SocketServer

class RoverServer:
    def __init__(self, communication):
        self.communication = communication
        self.communication.register_on_message_receive_callback(self.process_command)

    def process_command(self, command):
        print(f"Commande reçue par le Rover: {command}")
        response = f"Rover a exécuté: {command}"
        self.communication.send_message(response)

    def start(self):
        self.communication.start()

if __name__ == "__main__":
    communication = SocketServer()
    rover_server = RoverServer(communication)
    rover_server.start()
