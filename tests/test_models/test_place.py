#!/usr/bin/python3
"""Unittest for place class."""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """test case for the Place class."""

    def test_instance(self):
        """Test that a place instance can be created."""
        instance = Place()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
    