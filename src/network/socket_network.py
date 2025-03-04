import socket
from src.mars_rover.communication_server_interface import CommunicationServerInterface

class SocketNetwork(CommunicationServerInterface):
    def __init__(self, is_server: bool = False, host: str = 'localhost', port: int = 12345):
        self.is_server = is_server
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = None  # Pour stocker la connexion côté serveur

    def connect(self, host: str = None, port: int = None) -> None:
        if self.is_server:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            print(f"[Server] En attente de connexion sur {self.host}:{self.port}...")
            self.connection, addr = self.socket.accept()
            print(f"[Server] Connexion acceptée de {addr}")
        else:
            self.socket.connect((host or self.host, port or self.port))
            print(f"[Client] Connecté à {host or self.host}:{port or self.port}")

    def disconnect(self) -> None:
        if self.is_server and self.connection:
            self.connection.close()
        self.socket.close()
        print("[Socket] Connexion fermée")

    def send_message(self, recipient: str, message: str) -> None:
        data = f"{recipient}:{message}".encode()
        if self.is_server and self.connection:
            self.connection.sendall(data)
        else:
            self.socket.sendall(data)
        print(f"[Socket] Message envoyé: {message}")

    def receive_message(self) -> str:
        """
        Attend de recevoir un message et le retourne.
        """
        if self.is_server and self.connection:
            data = self.connection.recv(1024).decode()
        else:
            data = self.socket.recv(1024).decode()
        print(f"[Socket] Message reçu: {data}")
        return data

    def listen_for_messages(self, callback):
        """
        Écoute les messages entrants et appelle `callback(message)` pour les traiter.
        """
        print("[Socket] En attente de messages...")
        while True:
            message = self.receive_message()
            callback(message)
            if message.lower() == "shutdown":
                break
        self.disconnect()
