from network.socket_network import SocketNetwork
from mission_control.mission_control import MissionControl

if __name__ == "__main__":
    network = SocketNetwork(is_server=False)  # Mission Control agit comme un client
    mission_control = MissionControl(communication=network)
    mission_control.start()
