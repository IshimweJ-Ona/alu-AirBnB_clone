#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Simple tests for Amenity"""

    def test_instance(self):
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
