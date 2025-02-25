from ..mars_rover.communication_server_interface import CommunicationServerAbstract
import socket
import threading

class SocketServer(CommunicationServerAbstract):
    def __init__(self, host="localhost", port=8080):
        self.host = host
        self.port = port
        self.on_message_received = None
        self.server_socket = None
        self.running = False

    def register_on_message_receive_callback(self, on_message_received):
        """Enregistre le callback pour recevoir les messages."""
        self.on_message_received = on_message_received

    def send_message(self, message: str):
        """Envoie un message au client connecté."""
        print(f"[Network] Sending message: {message}")
        if hasattr(self, "client_socket") and self.client_socket:
            self.client_socket.send(message.encode())

    def start(self):
        """Démarre le serveur et écoute les connexions entrantes."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True
        print(f"[Network] Serveur démarré sur {self.host}:{self.port}")

        thread = threading.Thread(target=self._listen)
        thread.start()

    def _listen(self):
        """Attend les connexions et exécute le callback sur réception."""
        while self.running:
            client_socket, addr = self.server_socket.accept()
            self.client_socket = client_socket
            print(f"[Network] Connexion acceptée de {addr}")

            while self.running:
                try:
                    message = client_socket.recv(1024).decode()
                    if not message:
                        break
                    print(f"[Network] Message reçu: {message}")

                    # Appel du callback enregistré
                    if self.on_message_received:
                        self.on_message_received(message)

                except ConnectionResetError:
                    print(f"[Network] Connexion perdue avec {addr}")
                    break

            client_socket.close()
