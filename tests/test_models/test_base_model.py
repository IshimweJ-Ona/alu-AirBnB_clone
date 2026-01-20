#!/usr/bin/python3
"""Unittets for BaseModel class."""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test that a BaseModel instance can be created."""
        instance = BaseModel()
        self.assertIsNotNone(instance)

    def test_attributes_exist(self):
        """Test that id, created_at and updated_at exxist."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_id_is_string(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_is_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str_method(self):
        """Test representation format."""
        instance = BaseModel()
        string = str(instance)
        self.assertIn(instance.id, string)
        self.assertIn("BaseModel", string)

    def test_save_updates_updated_at(self):
        instance = BaseModel()
        old_time = instance.updated_at
        instance.save()
        self.assertNotEqual(old_time, instance.updated_at)

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        instance = BaseModel()
        self.assertIsInstance(instance.to_dict(), dict)

    def test_to_dict_contains_class(self):
        instance = BaseModel()
        self.assertIn("__class__", instance.to_dict())

    def test_to_dict_datetime_are_strings(self):
        instance = BaseModel()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary["created_at"], str)
        self.assertIsInstance(dictionary["updated_at"], str)

    def test_kwargs_reconstruction(self):
        """Test that instance can be reconstructed using kwargs."""
        instance = BaseModel()
        dictionary = instance.to_dict()
        new_instance = BaseModel(**dictionary)
        self.assertEqual(instance.id, new_instance.id)
        self.assertEqual(instance.created_at, new_instance.created_at)
        self.assertEqual(instance.updated_at, new_instance.updated_at)


if __name__ == "__main__":
    unittest.main()
    