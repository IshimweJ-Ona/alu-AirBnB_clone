#!/usr/bin/python3
"""Unittests for Place class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance(self):
        """Test that a Review instance can be created."""
        instance = Review()
        self.assertIsNotNone(instance)


if __name__ == "__main__":
    unittest.main()
