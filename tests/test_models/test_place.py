#!/usr/bin/python3
"""Unittests for Place class."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance(self):
        """Test that a Place instance can be created."""
        instance = Place()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
