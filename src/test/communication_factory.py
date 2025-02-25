# communication_factory.py
from socket_communication import SocketCommunication

def create_communication(role='server', host='localhost', port=8080):
    is_server = role == 'server'
    return SocketCommunication(host, port, is_server)
