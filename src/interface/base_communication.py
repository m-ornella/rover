from abc import ABC, abstractmethod
from typing import Optional, Callable

class BaseCommunicationServer(ABC):
    def __init__(self):
        self.connected = False

    @abstractmethod
    def connect(self, host: str, port: int) -> None:
        """Établit la connexion au serveur ou au client."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Ferme la connexion."""
        pass

    @abstractmethod
    def send_message(self, recipient: str, message: str) -> None:
        """Envoie un message à un destinataire spécifique."""
        pass

    @abstractmethod
    def receive_message(self) -> Optional[str]:
        """Attend de recevoir un message et le retourne."""
        pass

    def listen_for_messages(self, callback: Callable[[str], None]) -> None:
        """Écoute les messages entrants et appelle `callback(message)` pour les traiter."""
        print("[Communication] En attente de messages...")
        while self.connected:
            message = self.receive_message()
            if message:
                callback(message)
                if message.lower() == "shutdown":
                    break
        self.disconnect()
