import unittest
from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet

class TestMarsRover(unittest.TestCase):
    def setUp(self):
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)

    def test_initial_position(self):
        planet = ToroidalPlanet(10, 10)
        rover = MarsRover(0, 0, 'N', planet)
        self.assertEqual(rover.get_state(), "Position: (0, 0), Orientation: N")

    def test_move_forward_north(self):
        planet = ToroidalPlanet(10, 10)
        rover = MarsRover(0, 0, 'N', planet)
        rover.move_forward()
        self.assertEqual(rover.get_state(), "Position: (0, 1), Orientation: N")

    def test_turn_right(self):
        planet = ToroidalPlanet(10, 10)
        rover = MarsRover(0, 0, 'N', planet)
        rover.turn_right()
        self.assertEqual(rover.get_state(), "Position: (0, 0), Orientation: E")

    def test_wrap_around(self):
        planet = ToroidalPlanet(10, 10)
        rover = MarsRover(9, 0, 'N', planet)  # Start near the edge
        rover.move_forward()  # This should wrap around
        self.assertEqual(rover.get_state(), "Position: (9, 1), Orientation: N")

    def test_obstacle_detection(self):
        planet = ToroidalPlanet(10, 10, [(0, 1)])
        rover = MarsRover(0, 0, 'N', planet)
        rover.move_forward()
        self.assertEqual(rover.get_state(), "Position: (0, 0), Orientation: N")
        
if __name__ == '__main__':
    unittest.main()
