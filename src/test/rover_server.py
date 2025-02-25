# rover_server.py
from communication_interface import CommunicationInterface
from communication_factory import create_communication

class RoverServer:
    def __init__(self, communication: CommunicationInterface):
        self.communication = communication
        self.communication.register_on_message_receive_callback(self.process_command)

    def process_command(self, command):
        print(f"Commande reçue par le Rover: {command}")
        response = f"Rover a exécuté: {command}"
        self.communication.send_message(response)

    def start(self):
        self.communication.start()

if __name__ == "__main__":
    communication = create_communication(role='server')
    rover_server = RoverServer(communication)
    rover_server.start()
