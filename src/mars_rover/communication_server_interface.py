import abc

class CommunicationServerAbstract(abc.ABC):
    @abc.abstractmethod
    def register_on_message_receive_callback(self, on_message_received):
        """Enregistre un callback appelé lorsqu'un message est reçu."""
        pass

    @abc.abstractmethod
    def start(self):
        """Démarre le serveur de communication."""
        pass

    @abc.abstractmethod
    def send_message(self, message: str):
        """Envoie un message au client."""
        pass
