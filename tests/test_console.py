#!/usr/bin/python3
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Simple tests for the HBNBCommand console"""

    def setUp(self):
        """Set up a console instance before each test"""
        self.console = HBNBCommand()

    def test_quit_command(self):
        """Test that 'quit' command exits properly"""
        self.assertTrue(self.console.do_quit(""))

    def test_EOF_command(self):
        """Test that 'EOF' command exits properly"""
        self.assertTrue(self.console.do_EOF(""))

    def test_emptyline(self):
        """Test that emptyline does nothing"""
        self.assertIsNone(self.console.emptyline())


if __name__ == "__main__":
    unittest.main()
