#!/usr/bin/python3
"""Unittests for City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance(self):
        """Test that a City instance can be created."""
        instance = City()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
