import unittest
from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet

class TestMarsRover(unittest.TestCase):

    def test_initial_position(self):
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)
        self.assertEqual(self.rover.get_state(), "Position: (0, 0), Direction: N")

    def test_move_forward_north(self):
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)
        self.rover.move_forward()
        self.assertEqual(self.rover.get_state(), "Position: (0, 1), Direction: N")

    def test_turn_right(self):
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)
        self.rover.turn_right()
        self.assertEqual(self.rover.get_state(), "Position: (0, 0), Direction: E")

    def test_wrap_around(self):
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)
        self.rover.x = 9
        self.rover.move_forward()
        self.assertEqual(self.rover.get_state(), "Position: (9, 1), Direction: N")

if __name__ == '__main__':
    unittest.main()
