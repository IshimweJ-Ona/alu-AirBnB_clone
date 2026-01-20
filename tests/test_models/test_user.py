#!/usr/bin/python3
"""Unittest for User class."""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_instance(self):
        """Test that a User instance can be created."""
        instance = User()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
    