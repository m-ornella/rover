from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet

def main():
    width, height = 10, 10  # Taille de la planète
    obstacles = {(0,2),(4,2)}
    planet = ToroidalPlanet(width, height, obstacles)
    rover = MarsRover(0,0, 'N', planet)

    commands = "FFFF"
    
    for command in commands:
        if command == 'F':
            rover.move_forward()
        elif command == 'B':
            rover.move_backward()
        elif command == 'L':
            rover.turn_left()
        elif command == 'R':
            rover.turn_right()
        print(rover.get_state())

if __name__ == "__main__":
    main()
