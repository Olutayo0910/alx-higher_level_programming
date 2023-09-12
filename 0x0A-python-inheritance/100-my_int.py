#!/usr/bin/python3
"""module for myInt"""


class MyInt(int):
    """A int class"""
    def __eq__(self, other):
        """inverts operator =="""
        return int(self) != int(other)

    def __ne__(self, other):
        """inverts operator !="""
        return int(self) == int(other)
