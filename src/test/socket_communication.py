import socket
import threading
from communication_interface import CommunicationInterface

class SocketCommunication(CommunicationInterface):
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.callback = None
        self.running = False

    def start(self):
        """Démarre le serveur et accepte les connexions entrantes."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.running = True
        print(f"Serveur démarré sur {self.host}:{self.port}")

        threading.Thread(target=self._accept_connections).start()

    def _accept_connections(self):
        """Accepte les connexions des clients."""
        while self.running:
            self.client_socket, addr = self.server_socket.accept()
            print(f"Connexion acceptée de {addr}")
            threading.Thread(target=self._handle_client).start()

    def _handle_client(self):
        """Gère la communication avec le client connecté."""
        while self.running:
            try:
                message = self.receive_message()
                if message and self.callback:
                    self.callback(message)
            except ConnectionResetError:
                print("Connexion perdue.")
                break

    def send_message(self, message: str):
        """Envoie un message au client connecté."""
        if self.client_socket:
            self.client_socket.sendall(message.encode())
            print(f"Message envoyé: {message}")

    def receive_message(self) -> str:
        """Reçoit un message du client."""
        if self.client_socket:
            data = self.client_socket.recv(1024)
            if data:
                message = data.decode()
                print(f"Message reçu: {message}")
                return message
        return ""

    def register_callback(self, callback):
        """Enregistre une fonction de rappel pour les messages reçus."""
        self.callback = callback

    def stop(self):
        """Arrête le serveur."""
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
