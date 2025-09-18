#!/usr/bin/python3
"""
Unit tests for the basemodel class.
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Simple tests for BaseModel"""

    def test_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_has_id(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertIsInstance(obj.id, str)

    def test_created_and_updated_are_datetime(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def _test_str_method(self):
        obj = BaseModel()
        string = str(obj)
        self.assertIn("[BaseModel]", string)
        self.assertIn(obj.id, string)

    def test_save_updates_updated_at(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict_has_correct_keys(self):
        obj = BaseModel()
        d = obj.to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        datetime.fromisoformat(d["created_at"])
        datetime.fromisoformat(d["updated_at"])
        self.assertEqual(d["__class__"], "BaseModel")

    def test_init_from_kwargs(self):
        """Test if BaseModel can be reached from a dict (kwargs)."""
        obj = BaseModel()
        obj.name = "Test"
        obj.number = 123
        obj_dict = obj.to_dict()

        new_obj = BaseModel(**obj_dict)

        #check IDs match
        self.assertEqual(obj.id, new_obj.id)
        #created_at and updated_at 
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)
        #Extra attributes
        self.assertEqual(new_obj.name, "Test")
        self.assertEqual(new_obj.number, 123)


if __name__ == "__main__":
    unittest.main()
