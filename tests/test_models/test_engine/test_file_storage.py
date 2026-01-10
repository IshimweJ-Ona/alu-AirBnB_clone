#!/usr/bin/python3
"""Unittests for Place class."""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance(self):
        """Test that a Place instance can be created."""
        instance = FileStorage()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
