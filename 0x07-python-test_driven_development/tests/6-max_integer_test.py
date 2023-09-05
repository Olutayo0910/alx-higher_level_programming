#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for max_integer function."""

    def test_regular(self):
        """Test with a list of ints"""
        i = [1, 2, 3, 4, 5, 6]
        result = max_integer(i)
        self.assertEqual(result, 6)

    def test_not_int(self):
        """Test with list of non-ints and ints"""
        i = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, i)

    def test_empty(self):
        """Test with an empty list"""
        i = []
        result = max_integer(i)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values"""
        i = [-5, -4, -1]
        result = max_integer(i)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats"""
        i = [3, 4.5, 2]
        result = max_integer(i)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with a parameter that's not a list"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int"""
        i = [5]
        result = max_integer(i)
        self.assertEqual(result, 5)

    def test_identical(self):
        """Test with a list of identical values"""
        i = [6, 6, 6, 6, 6]
        result = max_integer(i)
        self.assertEqual(result, 6)

    def test_strings(self):
        """Test with a list of strings"""
        i = ["hi", "hello"]
        result = max_integer(i)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
