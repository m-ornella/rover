import unittest
from src.mars_rover import MarsRover
from src.toroidal_planet import ToroidalPlanet

class TestMarsRover(unittest.TestCase):
    def setUp(self):
        self.planet = ToroidalPlanet(10, 10)
        self.rover = MarsRover(0, 0, 'N', self.planet)

    def test_initial_position(self):
        self.assertEqual(self.rover.get_state(), "Position: (0, 0), Orientation: N")

    def test_move_forward(self):
        self.rover.move_forward()
        self.assertEqual(self.rover.get_state(), "Position: (0, 1), Orientation: N")

    def test_move_backward(self):
        self.rover.move_backward()
        self.assertEqual(self.rover.get_state(), "Position: (0, 9), Orientation: N")  # Toroïdal

    def test_turn_right(self):
        self.rover.turn_right()
        self.assertEqual(self.rover.get_state(), "Position: (0, 0), Orientation: E")

    def test_turn_left(self):
        self.rover.turn_left()
        self.assertEqual(self.rover.get_state(), "Position: (0, 0), Orientation: W")

    def test_wrap_around(self):
        self.rover.x = 9
        self.rover.move_forward()
        self.assertEqual(self.rover.get_state(), "Position: (9, 1), Orientation: N")

if __name__ == '__main__':
    unittest.main()
