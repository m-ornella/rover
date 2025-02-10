import asyncio
import websockets

class Network:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.clients = set()

    async def com_handler(self, websocket):
        """Gère les connexions WebSocket et transmet les messages entre clients."""
        self.clients.add(websocket)
        print(f"🚀 Nouveau client connecté. Total: {len(self.clients)}")

        try:
            async for message in websocket:
                # print(f"📩 Message reçu: {message}")

                # Trouver un autre client connecté
                other_clients = {client for client in self.clients if client != websocket}
                if other_clients:
                    # Envoyer le message à tous les autres clients connectés
                    await asyncio.gather(*(client.send(message) for client in other_clients))
                    # print(f"📤 Message relayé à {len(other_clients)} client(s).")
                else:
                    print("⚠️ Aucun autre client disponible pour relayer le message.")

        except websockets.exceptions.ConnectionClosed:
            print("❌ Un client s'est déconnecté.")

        finally:
            self.clients.discard(websocket)  # Utilisation de discard() pour éviter KeyError
            print(f"📉 Client déconnecté. Total: {len(self.clients)}")

    async def start(self):
        """Démarre le serveur WebSocket."""
        print(f"🚀 Serveur WebSocket en écoute sur ws://{self.host}:{self.port}")
        async with websockets.serve(self.com_handler, self.host, self.port):
            await asyncio.Future()  # Garde le serveur actif


