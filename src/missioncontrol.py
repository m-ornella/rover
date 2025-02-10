import asyncio
from .client import Client  # MissionControl utilise Client en interne

class MissionControl:
    def __init__(self):
        self.client = Client()  # Crée son propre client WebSocket

    async def run(self):
        """Boucle d'entrée utilisateur pour envoyer des commandes."""
        await self.client.connect()
        print("🛰️ Mission Control activé. Entrez des commandes (F, B, L, R) ou 'Q' pour quitter.")
        
        loop = asyncio.get_running_loop()
        while True:
            command = await loop.run_in_executor(None, input, ">> ")
            command = command.upper()
            
            if command == "Q":
                print("🔴 Fermeture de Mission Control.")
                await self.client.disconnect()
                break
            elif command in ["F", "B", "L", "R"]:
                response = await self.client.send(command)
                print(f"🔄 Réponse du rover: {response}")
            else:
                print("⚠️ Commande invalide. Utilisez seulement F, B, L, R.")
