#!/usr/bin/python3
"""Test file for BaseModel class."""


import unittest
from models.base_model imprt BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_instance(self):
        """Test that the basemodel instance can be created."""
        instance = BaseModel()
        self.assertIsNotNone(instance)


if __name__ == "__main__:
    unittest.main()
