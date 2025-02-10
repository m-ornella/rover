import asyncio
import threading
from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet
from src.obstacle import Obstacle
from src.network import Network
from src.missioncontrol import MissionControl

def start_network():
    """Démarre le serveur WebSocket dans un thread séparé."""
    network = Network()
    asyncio.run(network.start())

async def start_rover(rover):
    """Démarre le WebSocket client du rover."""
    await rover.run()  # Lance le rover en tâche de fond

async def start_mission_control():
    """Démarre Mission Control et envoie les commandes via WebSocket."""
    mission_control = MissionControl()  # MissionControl gère son propre Client
    await mission_control.run()

async def main():
    # Initialisation de la planète et du rover
    width, height = 10, 10
    obstacles = {
        Obstacle(0, 2, "cailloux"),
        Obstacle(4, 2, "trou")
    }
    planet = ToroidalPlanet(width, height, obstacles)
    rover = MarsRover(0, 0, 'N', planet)  # Le rover gère son propre Client

    # Démarrer le serveur WebSocket dans un thread séparé
    network_thread = threading.Thread(target=start_network, daemon=True)
    network_thread.start()

    # 🔥 Attendre que le serveur WebSocket soit prêt avant de lancer les clients
    await asyncio.sleep(1)  # Attente asynchrone pour éviter "ConnectionRefusedError"

    # Lancer le rover et Mission Control dans une boucle asyncio
    tasks = [
        asyncio.create_task(start_rover(rover)),
        asyncio.create_task(start_mission_control())
    ]

    # Attendre que tout soit terminé
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())  # Lancer proprement la boucle asyncio
