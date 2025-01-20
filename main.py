from rover.classes.mars_rover import MarsRover
from rover.classes.toroidal_planet import ToroidalPlanet

def main():
    width, height = 10, 10  # Taille de la planète
    planet = ToroidalPlanet(width, height)
    rover = MarsRover(0, 0, 'N', planet)

    commands = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
    
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
