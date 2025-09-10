import unittest
import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Text_align")))
 
from util import text_aligning
 
class TestHackerRankLogo(unittest.TestCase):
 
    def test_sample_input_5(self):
        expected_start = [
            "    H    ",
            "   HHH   ",
            "  HHHHH  ",
            " HHHHHHH ",
            "HHHHHHHHH"
        ]
        result = text_aligning(5)
        self.assertTrue(result[0:5] == expected_start)
 
    def test_invalid_even_thickness(self):
        with self.assertRaises(ValueError):
            text_aligning(4)

    def test_invalid_even_thickness(self):
        with self.assertRaises(ValueError):
            text_aligning(4)
 
if __name__ == "__main__":
    unittest.main()