from abc import ABC, abstractmethod

class CommunicationInterface(ABC):
    @abstractmethod
    def start(self):
        """Démarre le service de communication."""
        pass

    @abstractmethod
    def send_message(self, message: str):
        """Envoie un message."""
        pass

    @abstractmethod
    def receive_message(self) -> str:
        """Reçoit un message."""
        pass

    @abstractmethod
    def register_callback(self, callback):
        """Enregistre une fonction de rappel pour les messages reçus."""
        pass
