#!/usr/bin/python3
# Boakye
""" File name : 10-square.py
    It is not allowed to import any module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square -- Multiple inheritance"""
    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
