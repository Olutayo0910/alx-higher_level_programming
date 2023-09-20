#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

class TestSquare(unittest.TestCase):

    def setUp(self):
        """Set up a Square object for testing."""
        self.square = Square(5, 1, 2, 10)

    def tearDown(self):
        """Clean up the Square object after testing."""
        self.square = None

    def test_initialization(self):
        """Test initializing a Square object."""
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)
        self.assertEqual(self.square.id, 10)

    def test_size_getter_setter(self):
        """Test size getter and setter methods."""
        self.square.size = 6
        self.assertEqual(self.square.size, 6)

    def test_string_representation(self):
        """Test string representation of Square."""
        self.assertEqual(str(self.square), "[Square] (10) 1/2 - 5")

    def test_update(self):
        """Test the update method of Square."""
        self.square.update(20, 4, 5, 6)
        self.assertEqual(self.square.size, 4)
        self.assertEqual(self.square.x, 5)
        self.assertEqual(self.square.y, 6)
        self.assertEqual(self.square.id, 20)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square."""
        square_dict = self.square.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
