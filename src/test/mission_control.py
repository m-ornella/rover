# mission_control.py
from socket_communication import SocketClient
import time

class MissionControl:
    def __init__(self, communication):
        self.communication = communication
        self.communication.register_on_message_receive_callback(self.receive_response)

    def send_command(self, command: str):
        print(f"Envoi de la commande: {command}")
        self.communication.send_message(command)

    def receive_response(self, message):
        print(f"Réponse du Rover: {message}")

    def start(self):
        self.communication.start()

if __name__ == "__main__":
    communication = SocketClient()
    mission_control = MissionControl(communication)
    mission_control.start()

    # Envoi de quelques commandes avec un délai pour illustrer
    time.sleep(1)
    mission_control.send_command("Avancer")
    time.sleep(1)
    mission_control.send_command("Tourner à gauche")
   
 
