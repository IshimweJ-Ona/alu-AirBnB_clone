#!/usr/bin/python3
"""Unittest for State class."""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the state class."""

    def test_instance(self):
        """Test that a state instance can be created."""
        instance = State()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
    