import abc

class CommunicationServerAbstract(abc.ABC):
    @abc.abstractmethod
    def register_on_message_receive_callback(self, on_message_received):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def send_message(self, message: str):
        pass