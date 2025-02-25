import socket
import time

class MissionControl:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        """Se connecte au serveur du Rover."""
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connecté au Rover sur {self.host}:{self.port}")

    def send_command(self, command: str):
        """Envoie une commande au Rover et affiche la réponse."""
        if self.client_socket:
            self.client_socket.sendall(command.encode())
            print(f"Commande envoyée: {command}")
            response = self.client_socket.recv(1024).decode()
            print(f"Réponse reçue: {response}")

    def disconnect(self):
        """Ferme la connexion avec le serveur du Rover."""
        if self.client_socket:
            self.client_socket.close()

if __name__ == "__main__":
    mission_control = MissionControl()
    mission_control.connect()
    mission_control.send_command("Avancer")
    time.sleep(1)
    mission_control.send_command("Tourner à gauche")
    mission_control.disconnect()
