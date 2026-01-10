#!/usr/bin/python3
"""Unittests for Place class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance(self):
        """Test that a State instance can be created."""
        instance = State()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
