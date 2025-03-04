from src.mars_rover.communication_server_interface import CommunicationServerInterface

class MissionControl:
    def __init__(self, communication: CommunicationServerInterface):
        self.communication = communication

    def start(self):
        print("[Mission Control] Connexion au rover...")
        self.communication.connect()

        def handle_message(message):
            print(f"[Mission Control] Réponse du rover: {message}")

        while True:
            command = input("Entrez une commande pour le rover: ")
            self.communication.send_message("rover", command)
            if command.lower() == "q":
                print("[Mission Control] Fermeture de la connexion.")
                break

            # Écoute la réponse du rover après chaque commande
            self.communication.listen_for_messages(handle_message)

        self.communication.disconnect()
