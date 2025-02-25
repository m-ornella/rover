# socket_communication.py
import socket
import threading
from communication_interface import CommunicationInterface

class SocketServer(CommunicationInterface):
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.callback = None
        self.running = False

    def register_on_message_receive_callback(self, callback):
        self.callback = callback

    def start(self):
        """Démarre le serveur et accepte les connexions entrantes."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        self.running = True
        print(f"Serveur démarré sur {self.host}:{self.port}")

        threading.Thread(target=self._accept_connections).start()

    def _accept_connections(self):
        while self.running:
            self.client_socket, addr = self.server_socket.accept()
            print(f"Connexion acceptée de {addr}")
            threading.Thread(target=self._handle_client, args=(self.client_socket,)).start()

    def _handle_client(self, client_socket):
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

    def send_message(self, message: str):
        if self.client_socket:
            self.client_socket.sendall(message.encode())
            print(f"Message envoyé: {message}")

    def stop(self):
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()

class SocketClient(CommunicationInterface):
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.client_socket = None
        self.callback = None

    def register_on_message_receive_callback(self, callback):
        self.callback = callback

    def start(self):
        """Se connecte au serveur."""
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connecté au serveur {self.host}:{self.port}")

        threading.Thread(target=self._receive_messages).start()

    def _receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(f"Message reçu du serveur: {message}")
                    if self.callback:
                        self.callback(message)
                else:
                    break
            except ConnectionResetError:
                break
        self.client_socket.close()

    def send_message(self, message: str):
        if self.client_socket:
            self.client_socket.sendall(message.encode())
            print(f"Message envoyé au serveur: {message}")

    def stop(self):
        if self.client_socket:
            self.client_socket.close()
