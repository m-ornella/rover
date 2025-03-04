from src.mars_rover.communication_server_interface import CommunicationServerInterface
from src.mars_rover.rover_interface import IRover

class RoverServer:
    def __init__(self, communication: CommunicationServerInterface, rover: IRover):
        self.communication = communication
        self.rover = rover
        
    def start(self):
        print("[Rover] Démarrage du serveur...")
        self.communication.connect()
        self.communication.listen_for_messages(self.handle_message)

    def handle_message(self, message: str):
        """
        Traite une commande reçue et renvoie la position du Rover.
        """
        print(f"[Rover] Commande reçue: {message}")

        # Vérifie quelle commande a été envoyée
        command = message.strip().upper()

        if command == "F":
            self.rover.move_forward()
        elif command == "B":
            self.rover.move_backward()
        elif command == "L":
            self.rover.turn_left()
        elif command == "R":
            self.rover.turn_right()
        elif command == "Q":
            print("[Rover] Arrêt du serveur demandé.")
            self.communication.disconnect()
            return
        else:
            print("[Rover] Commande inconnue.")

        # Récupère l'état actuel du rover et l'envoie en réponse
        state = self.rover.get_state()
        self.communication.send_message("mission_control", state)