#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Simple tests for Place"""

    def test_instance(self):
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
