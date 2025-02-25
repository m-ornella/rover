from communication_interface import CommunicationInterface

class RoverServer:
    def __init__(self, communication: CommunicationInterface):
        self.communication = communication
        self.communication.register_callback(self.process_command)

    def process_command(self, command: str):
        """Traite la commande reçue et envoie une réponse."""
        print(f"Commande reçue: {command}")
        response = f"Commande '{command}' exécutée."
        self.communication.send_message(response)

    def start(self):
        """Démarre le serveur de communication."""
        self.communication.start()

if __name__ == "__main__":
    from socket_communication import SocketCommunication
    comm = SocketCommunication()
    rover_server = RoverServer(comm)
    rover_server.start()
