#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Simple tests for City"""

    def test_instance(self):
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
