#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Simple tests for State"""

    def test_instance(self):
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
