from mars_rover.communication_server_interface import CommunicationServerAbstract
from network.socket_server import SocketServer  # Importer ton fichier réseau


class RoverServer:
    def __init__(self, communication_server: CommunicationServerAbstract):
        self.communication_server = communication_server
        self.communication_server.register_on_message_receive_callback(self.process_command)

    def on_message_received(self, command):
        """Traite une commande reçue et envoie une réponse."""
        print(f"[Rover] Commande reçue: {command}")
        
        response = f"Executed: {command}"
        self.communication_server.send_message(response)

    def start(self):
        """Démarre le serveur de communication (ex: SocketServer)."""
        self.communication_server.start()

if __name__ == "__main__":
    socket_server = SocketServer()
    rover = RoverServer(socket_server)
    rover.start()
