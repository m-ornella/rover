import socket

class MissionControl:
    def __init__(self, rover_host="localhost", rover_port=8080):
        self.rover_host = rover_host
        self.rover_port = rover_port

    def send_command(self, command):
        """Envoie une commande au Rover via le réseau."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.rover_host, self.rover_port))
            s.send(command.encode())
            response = s.recv(1024).decode()
            print(f"[MissionControl] Réponse reçue: {response}")

if __name__ == "__main__":
    mission_control = MissionControl()
    mission_control.send_command("Move Forward")
    mission_control.send_command("Turn Left")
