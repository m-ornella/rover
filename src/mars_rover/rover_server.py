from src.mars_rover.communication_server_interface import CommunicationServerInterface

class RoverServer:
    def __init__(self, communication: CommunicationServerInterface):
        self.communication = communication

    def start(self):
        print("[Rover] Démarrage du serveur...")
        self.communication.connect()
        print("[Rover] En attente de messages...")
        while True:
            message = self.communication.receive_message("mission_control")
            if message.lower() == "shutdown":
                print("[Rover] Arrêt du serveur.")
                break
            print(f"[Rover] Message reçu: {message}")
        self.communication.disconnect()