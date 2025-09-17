#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Simple tests for Review"""

    def test_instance(self):
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()
