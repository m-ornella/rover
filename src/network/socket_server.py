import socket

from ..mars_rover import CommunicationServerAbstract

class SocketServer(CommunicationServerAbstract):
    def __init__(self):
        self.on_message_received = None
        self.buffer = None
        self.running = False

    def register_on_message_receive_callback(self, on_message_received):
        self.on_message_received = on_message_received

    def send_message(self, message: str):
        print(f"[Network] Sending message: {message}")
        self.buffer = message  # Simule un envoi de message

    def start(self):
        """Démarre un thread qui écoute les messages entrants."""
        self.running = True
        thread = threading.Thread(target=self._listen, daemon=True)
        thread.start()

    def _listen(self):
        """Simule un serveur écoutant en permanence et appelant le callback."""
        while self.running:
            if self.buffer and self.on_message_received:
                print(f"[Network] Message received: {self.buffer}")
                self.on_message_received(self.buffer)  # Appel du callback
                self.buffer = None  # Vide le buffer après réception
                time.sleep(0.5)  # Simule un délai réseau
