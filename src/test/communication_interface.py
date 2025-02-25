# communication_interface.py
import abc

class CommunicationInterface(abc.ABC):
    @abc.abstractmethod
    def register_on_message_receive_callback(self, callback):
        """Enregistre un callback appelé lors de la réception d'un message."""
        pass

    @abc.abstractmethod
    def start(self):
        """Démarre le service de communication."""
        pass

    @abc.abstractmethod
    def send_message(self, message: str):
        """Envoie un message à l'autre partie."""
        pass
