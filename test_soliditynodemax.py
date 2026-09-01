# test_soliditynodemax.py
"""
Tests for SolidityNodeMax module.
"""

import unittest
from soliditynodemax import SolidityNodeMax

class TestSolidityNodeMax(unittest.TestCase):
    """Test cases for SolidityNodeMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityNodeMax()
        self.assertIsInstance(instance, SolidityNodeMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityNodeMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
