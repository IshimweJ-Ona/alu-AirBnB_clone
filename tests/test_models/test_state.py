#!/usr/bin/python3
"""Unittests for State class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance(self):
        """Test that a State instance can be created."""
        state = State()
        self.assertIsNone(state)
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """Test default public attributes of State."""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
