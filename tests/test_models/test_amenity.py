#!/usr/bin/python3
"""Unittests for Place class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance(self):
        """Test that a Amenity instance can be created."""
        instance = Amenity()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
