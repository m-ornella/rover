from typing import Protocol

class CommunicationServerInterface(Protocol):
    def connect(self, host: str, port: int) -> None:
        """
        Établit une connexion en tant que client ou démarre un serveur.
        
        :param host: Adresse IP ou hostname.
        :param port: Port utilisé pour la communication.
        """
        pass

    def disconnect(self) -> None:
        """
        Ferme proprement la connexion au serveur ou arrête le serveur.
        """
        pass

    def send_message(self, recipient: str, message: str) -> None:
        """
        Envoie un message à un destinataire spécifique.
        
        :param recipient: Identifiant du destinataire (ex: "rover" ou "mission_control").
        :param message: Contenu du message à envoyer.
        """
        pass

    def receive_message(self, sender: str) -> str:
        """
        Reçoit un message d'un expéditeur spécifique.
        
        :param sender: Identifiant de l'expéditeur (ex: "rover" ou "mission_control").
        :return: Contenu du message reçu.
        """
        pass
