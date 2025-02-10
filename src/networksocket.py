import asyncio
import websockets

class NetworkSocket:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.clients = set()

    async def handler(self, websocket, path):  # 🔥 Ajout du paramètre `path`
        """Gère les connexions WebSocket et transmet les commandes au rover."""
        self.clients.add(websocket)
        print(f"🚀 Nouveau client connecté. Total clients: {len(self.clients)}")

        try:
            async for msg in websocket:
                print(f"📩 Commande reçue: {msg}")

                # Simuler l'exécution de la commande et renvoyer une réponse
                response = f"Rover a exécuté: {msg}"
                
                # Envoi de la réponse au client
                await websocket.send(response)

        except websockets.exceptions.ConnectionClosed:
            print("❌ Client déconnecté.")

        finally:
            self.clients.remove(websocket)
            print(f"📉 Client déconnecté. Total clients: {len(self.clients)}")

    async def start(self):
        """Démarre le serveur WebSocket."""
        print(f"🚀 Serveur WebSocket en écoute sur ws://{self.host}:{self.port}")
        async with websockets.serve(self.handler, self.host, self.port):  # Assurez-vous que `self.handler` est bien utilisé ici
            await asyncio.Future()  # Maintient le serveur en exécution
