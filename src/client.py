import websockets

class Client():
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.websocket = None

    async def connect(self):
        """Connecte le client au serveur WebSocket."""
        self.websocket = await websockets.connect(f"ws://{self.host}:{self.port}")
        print("🔗 Connecté au serveur WebSocket.")

    async def send(self, message):
        """Envoie un message et récupère la réponse du serveur."""
        await self.websocket.send(message)
        # print(f"📤 Message envoyé: {message}")
        return await self.receive()  # Retourne la réponse

    async def receive(self):
        """Reçoit un message du serveur WebSocket."""
        response = await self.websocket.recv()
        # print(f"📩 Réponse reçue: {response}")
        return response  # Retourne la réponse

    async def disconnect(self):
        """Déconnecte le client du serveur WebSocket."""
        await self.websocket.close()
        print("❌ Déconnecté du serveur WebSocket.")
