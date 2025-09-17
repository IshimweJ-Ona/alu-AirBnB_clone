#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Simple tests for BaseModel"""

    def test_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_has_id(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))

    def test_has_created_at(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "created_at"))

    def test_has_updated_at(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "updated_at"))


if __name__ == "__main__":
    unittest.main()

