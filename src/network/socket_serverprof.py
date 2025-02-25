from ..mars_rover import CommunicationServerAbstract

class SocketServer(CommunicationServerAbstract):
    def register_on_message_receive_callback(self, on_message_received):
        self.__callback = on_message_received

    def start(self):
        socket.on_message_received(self.__callback)
        socket.startListening()
        pass