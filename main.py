from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet
from src.orientation import Orientation

def main():
    width, height = 10, 10  # Taille de la planète
    planet = ToroidalPlanet(width, height)

    initial_orientation = 'N'

    rover = MarsRover(0, 0, initial_orientation, planet)

    commands = "FFBRFLB"
    
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
