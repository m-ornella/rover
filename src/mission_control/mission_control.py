import threading
from src.interface.communication_server_interface import CommunicationServerInterface

class MissionControl:
    def __init__(self, communication: CommunicationServerInterface):
        self.communication = communication

    def start(self):
        print("[Mission Control] Connexion au rover...")
        self.communication.connect()

        def handle_message(message):
            print(f"[Mission Control] Réponse du rover: {message}")
        
        # Fonction pour gérer les entrées utilisateur
        def get_user_input():
            while True:
                command = input("Entrez une commande pour le rover: ")
                self.communication.send_message("rover", command)
                if command.lower() == "q":
                    print("[Mission Control] Fermeture de la connexion.")
                    self.communication.disconnect()
                    break

        # Démarrer le thread pour écouter les messages
        listener_thread = threading.Thread(target=self.communication.listen_for_messages, args=(handle_message,))
        listener_thread.daemon = True  # S'assurer que le thread se termine lorsque le programme principal termine
        listener_thread.start()

        # Gérer l'entrée utilisateur dans le thread principal
        get_user_input()
