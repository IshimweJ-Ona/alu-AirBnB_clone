#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Simple tests for User"""

    def test_instance(self):
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
