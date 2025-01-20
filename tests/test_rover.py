import unittest
from rover.classes.mars_rover import MarsRover
from rover.classes.toroidal_planet import ToroidalPlanet

class TestMarsRover(unittest.TestCase):
    def setUp(self):
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)

    def test_initial_position(self):
        self.assertEqual(self.rover.get_state(), "Position: (0, 0), Direction: N")

    def test_move_forward_north(self):
        self.rover.move_forward()
        self.assertEqual(self.rover.get_state(), "Position: (0, 1), Direction: N")

    def test_turn_right(self):
        self.rover.turn_right()
        self.assertEqual(self.rover.get_state(), "Position: (0, 0), Direction: E")

    def test_wrap_around(self):
        self.rover.x = 9
        self.rover.move_forward()
        self.assertEqual(self.rover.get_state(), "Position: (9, 1), Direction: N")

if __name__ == '__main__':
    unittest.main()
