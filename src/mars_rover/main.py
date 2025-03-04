from src.network.socket_network import SocketNetwork
from src.mars_rover.rover_server import RoverServer



network = SocketNetwork(is_server=True)
rover = RoverServer(network)
rover.start()
