from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet
from src.obstacle import Obstacle

def main():
    width, height = 10, 10
    obstacles = {
        Obstacle(0, 2, "cailloux"),
        Obstacle(4, 2, "trou")
    }
    planet = ToroidalPlanet(width, height, obstacles)
    rover = MarsRover(0,0, 'N', planet)

    while True:
        commands = input("Entrez une séquence de commandes (F, B, L, R) ou 'Q' pour quitter: ").upper()

        if commands == 'Q':
            print("Fin. État du rover:", rover.get_state())
            break

        for command in commands:
            if command == 'F':
                rover.move_forward()
            elif command == 'B':
                rover.move_backward()
            elif command == 'L':
                rover.turn_left()
            elif command == 'R':
                rover.turn_right()
            else:
                print(f"Commande invalide: {command}. Utilisez uniquement F, B, L, R.")
        
            print(rover.get_state())
    
if __name__ == "__main__":
    main()