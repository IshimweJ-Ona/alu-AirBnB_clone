#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Simple tests for the FileStorage class"""

    def setUp(self):
        """Set up a FileStorage instance before each test"""
        self.storage = FileStorage()

    def test_instance_creation(self):
        """Test that FileStorage instance is created"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_reload_method_exists(self):
        """Test that reload method exists and runs without error"""
        self.assertTrue(hasattr(self.storage, "reload"))
        self.assertIsNone(self.storage.reload())


if __name__ == "__main__":
    unittest.main()
