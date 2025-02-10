import json
from .rover_interface import IRover
from .toroidal_planet import ToroidalPlanet
from .movement import Movement
from .client import Client  # 🔹 Importation du client WebSocket

class MarsRover(IRover):
    def __init__(self, x: int, y: int, orientation: str, planet: ToroidalPlanet):
        self.x = x
        self.y = y
        self.orientation_handler = Movement(orientation)
        self.planet = planet
        self.client = Client()  # 🔹 Instanciation du Client WebSocket interne

    def move_forward(self):
        new_x, new_y = self.orientation_handler.move_forward(self.x, self.y)
        new_x, new_y = self.planet.wrap_coordinates(new_x, new_y)
        if self.planet.is_obstacle(new_x, new_y):
            return "⚠️ Rover bloqué"
        self.x, self.y = new_x, new_y
        return '✅ Avancé'

    def move_backward(self):
        new_x, new_y = self.orientation_handler.move_backward(self.x, self.y)
        new_x, new_y = self.planet.wrap_coordinates(new_x, new_y)
        if self.planet.is_obstacle(new_x, new_y):
            return "⚠️ Rover bloqué"
        self.x, self.y = new_x, new_y
        return "✅ Reculé"

    def turn_left(self):
        self.orientation_handler.turn_left()
        return "✅ Tourné à gauche"

    def turn_right(self):
        self.orientation_handler.turn_right()
        return "✅ Tourné à droite"

    def get_state(self):
        return {"x": self.x, "y": self.y, "orientation": str(self.orientation_handler)}

    def execute_command(self, command):
        if command == "F":
            result = self.move_forward()
        elif command == "B":
            result = self.move_backward()
        elif command == "L":
            result = self.turn_left()
        elif command == "R":
            result = self.turn_right()
        else:
            result = "Commande invalide."

        return {"status": result, **self.get_state()}

    async def connect(self):
        """Démarre la connexion WebSocket et écoute les commandes."""
        await self.client.connect()  # 🔹 Connexion WebSocket via Client

        try:
            while True:
                command = await self.client.receive()  # 🔹 Réception des commandes du serveur
                # print(f"📩 Commande reçue: {command}")
                response = self.execute_command(command)
                await self.client.send(json.dumps(response, ensure_ascii=False))  # 🔹 Envoi de la réponse
        except Exception as e:
            print(f"Erreur: {e}")
        finally:
            await self.client.disconnect()  # 🔹 Déconnexion propre

    async def run(self):
        """Démarre le rover en tâche de fond."""
        await self.connect()

