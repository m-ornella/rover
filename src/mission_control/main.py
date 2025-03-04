from src.network.socket_network import SocketNetwork
from src.mission_control.mission_control import MissionControl

network = SocketNetwork(is_server=False)
mission = MissionControl(network)
mission.start()

