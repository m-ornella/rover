# socket_communication.py
import socket
import threading
from communication_interface import CommunicationInterface

class SocketCommunication(CommunicationInterface):
    def __init__(self, host='localhost', port=8080, is_server=False):
        self.host = host
        self.port = port
        self.is_server = is_server
        self.socket = None
        self.client_socket = None
        self.callback = None
        self.running = False

    def register_on_message_receive_callback(self, callback):
        self.callback = callback

    def start(self):
        """Démarre le service de communication."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        if self.is_server:
            self.socket.bind((self.host, self.port))
            self.socket.listen(2)
            self.running = True
            print(f"Serveur démarré sur {self.host}:{self.port}")
            threading.Thread(target=self._accept_connections).start()
        else:
            self.socket.connect((self.host, self.port))
            print(f"Connecté au serveur {self.host}:{self.port}")
            threading.Thread(target=self._receive_messages).start()

    def _accept_connections(self):
        while self.running:
            """Accepte les connexions entrantes."""
            self.client_socket, addr = self.socket.accept()
            print(f"Connexion acceptée de {addr}")
            threading.Thread(target=self._handle_client, args=(self.client_socket,)).start()

    def _handle_client(self, client_socket):
        """Gère la communication avec le client."""
        while self.running:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Message reçu: {message}")
                    if self.callback:
                        self.callback(message)
                else:
                    break
            except ConnectionResetError:
                break
        client_socket.close()

    def _receive_messages(self):
        """Reçoit les messages du serveur."""
        while self.running:
            try:
                message = self.socket.recv(1024).decode()
                if message:
                    print(f"Message reçu du serveur: {message}")
                    if self.callback:
                        self.callback(message)
                else:
                    break
            except ConnectionResetError:
                break
        

    def send_message(self, message: str):
        """Envoie un message à l'autre partie."""
        if self.socket and self.socket.fileno() != -1:  # Ensure socket is open
            if self.is_server and self.client_socket:
                self.client_socket.sendall(message.encode())
                print(f"Message envoyé au client: {message}")
            elif not self.is_server:
                self.socket.sendall(message.encode())
                print(f"Message envoyé au serveur: {message}")
        else:
            print("Erreur: Le socket est fermé ou invalide.")
            # Handle reconnection or other recovery mechanisms here

    def stop(self):
        """Arrête le service de communication."""
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.socket:
            self.socket.close()
