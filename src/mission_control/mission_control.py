from src.mars_rover.communication_server_interface import CommunicationServerInterface

class MissionControl:
    def __init__(self, communication: CommunicationServerInterface):
        self.communication = communication

    def start(self):
        print("[Mission Control] Connexion au rover...")
        self.communication.connect()
        while True:
            command = input("Entrez une commande pour le rover: ")
            self.communication.send_message("rover", command)
            if command.lower() == "shutdown":
                print("[Mission Control] Fermeture de la connexion.")
                break
        self.communication.disconnect()

