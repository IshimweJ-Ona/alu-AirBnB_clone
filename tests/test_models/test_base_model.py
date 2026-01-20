#!/usr/bin/python3
"""Unittets for BaseModel class."""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test cases for the BaseModel class."""

    def test_instance(self):
        """Test that a BaseModel instance can be created."""
        instance = BaseModel()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
    