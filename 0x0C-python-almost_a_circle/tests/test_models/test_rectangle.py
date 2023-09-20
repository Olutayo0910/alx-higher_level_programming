#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import unittest.mock


class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        """Test initializing a Rectangle object."""
        r = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_width_setter(self):
        """Test the width setter method."""
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_width_invalid_type(self):
        """Test setting width with an invalid type."""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = "invalid"

    def test_width_invalid_value(self):
        """Test setting width with an invalid value."""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height_setter(self):
        """Test the height setter method."""
        r = Rectangle(10, 20)
        r.height = 25
        self.assertEqual(r.height, 25)

    def test_height_invalid_type(self):
        """Test setting height with an invalid type."""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.height = "invalid"

    def test_height_invalid_value(self):
        """Test setting height with an invalid value."""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -5

    def test_x_setter(self):
        """Test the x setter method."""
        r = Rectangle(10, 20)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_x_invalid_type(self):
        """Test setting x with an invalid type."""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.x = "invalid"

    def test_x_invalid_value(self):
        """Test setting x with an invalid value."""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.x = -5

    def test_y_setter(self):
        """Test the y setter method."""
        r = Rectangle(10, 20)
        r.y = 5
        self.assertEqual(r.y, 5)

    def test_y_invalid_type(self):
        """Test setting y with an invalid type."""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.y = "invalid"

    def test_y_invalid_value(self):
        """Test setting y with an invalid value."""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.y = -5

    def test_area(self):
        """Test calculating the area of the rectangle."""
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        """Test displaying the rectangle."""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        """Test updating attributes of the rectangle."""
        r = Rectangle(10, 20, 1, 2, 100)
        r.update(101, 5, 6, 7, 8)
        self.assertEqual(r.id, 101)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)

    def test_update_kwargs(self):
        """Test updating attributes of the rectangle using keyword arguments."""
        r = Rectangle(10, 20, 1, 2, 100)
        r.update(id=101, width=5, height=6, x=7, y=8)
        self.assertEqual(r.id, 101)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)

    def test_to_dictionary(self):
        """Test creating a dictionary representation of the rectangle."""
        r = Rectangle(10, 20, 1, 2, 100)
        r_dict = r.to_dictionary()
        expected_dict = {'id': 100, 'width': 10, 'height': 20, 'x': 1, 'y': 2}
        self.assertEqual(r_dict, expected_dict)

    def test_str(self):
        """Test the string representation of the rectangle."""
        r = Rectangle(10, 20, 1, 2, 100)
        expected_str = '[Rectangle] (100) 1/2 - 10/20'
        self.assertEqual(str(r), expected_str)

if __name__ == '__main__':
    unittest.main()
