from src.network.socket_network import SocketNetwork
from src.mars_rover.rover_server import RoverServer
from src.mars_rover.mars_rover import MarsRover
from src.toroidal_planet.toroidal_planet import ToroidalPlanet

if __name__ == "__main__":
   
    # Création de la communication réseau
    network = SocketNetwork(is_server=True)

    # Création du rover avec une planète de taille 10x10 avec obstacles
    planet = ToroidalPlanet(width=10, height=10, obstacles=[(3, 3), (5, 5)])
    mars_rover = MarsRover(x=0, y=0, orientation="N", planet=planet)

    # Instanciation du serveur avec la communication et le rover
    rover_server = RoverServer(communication=network, rover=mars_rover)

    # Démarrage du serveur
    rover_server.start()
