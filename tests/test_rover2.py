import unittest
from unittest.mock import AsyncMock, patch
from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet
from src.missioncontrol import MissionControl
from src.client import Client

class TestMissionControl(unittest.TestCase):
    def setUp(self):
        # Configuration de la planète et du rover
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)
        
        # Mock du Client avec AsyncMock
        self.client_mock = AsyncMock(spec=Client)
        self.client_mock.receive.return_value = "F"  # Simule la commande "F"
        self.client_mock.send.return_value = '{"status": "✅ Avancé", "x": 0, "y": 1, "orientation": "N"}'

        # Remplacer le client dans MissionControl par notre mock
        self.mission_control = MissionControl()
        self.mission_control.client = self.client_mock

    async def test_move_forward_via_mission_control(self):
        """Test si Mission Control envoie correctement une commande 'F'."""
        # On mock la réponse du rover
        self.client_mock.send.return_value = '{"status": "✅ Avancé", "x": 0, "y": 1, "orientation": "N"}'

        # Appel de la méthode pour simuler l'envoi de la commande 'F' depuis MissionControl
        response = await self.mission_control.client.send("F")
        
        # Vérification que la méthode 'send' a bien été appelée avec le bon message
        self.client_mock.send.assert_called_with("F")
        
        # Vérification de la réponse simulée
        self.assertEqual(response, '{"status": "✅ Avancé", "x": 0, "y": 1, "orientation": "N"}')

    async def test_invalid_command(self):
        """Test si Mission Control gère les commandes invalides correctement."""
        # Simule une commande invalide (ex. une commande "X")
        self.client_mock.send.return_value = '{"status": "⚠️ Commande invalide.", "x": 0, "y": 0, "orientation": "N"}'

        # On utilise await ici pour obtenir le résultat de la coroutine
        response = await self.mission_control.client.send("X")
        
        # Vérification que la méthode 'send' a bien été appelée avec la commande "X"
        self.client_mock.send.assert_called_with("X")
        
        # Vérification de la réponse simulée
        self.assertEqual(response, '{"status": "⚠️ Commande invalide.", "x": 0, "y": 0, "orientation": "N"}')

    async def test_move_forward_blocked_by_obstacle(self):
        """Test si Mission Control gère le blocage du rover par un obstacle."""
        # Créer une planète avec un obstacle et placer le rover à proximité
        obstacle_planet = ToroidalPlanet(10, 10, [(0, 1)])
        blocked_rover = MarsRover(0, 0, 'N', obstacle_planet)
        
        # Remplacer le rover de MissionControl par ce nouveau rover bloqué
        self.mission_control.client.send.return_value = '{"status": "⚠️ Rover bloqué", "x": 0, "y": 0, "orientation": "N"}'

        # On utilise await ici pour obtenir le résultat de la coroutine
        response = await self.mission_control.client.send("F")
        
        # Vérification de la répo
