import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Print_format")))
from util import capture_output

class TestMutateString(unittest.TestCase):
 
    def test_print_formatted_1(self):
        self.assertEqual(capture_output(2)[0].split(), ["1","1","1","1"])
    def test_print_formatted_2(self):
        self.assertEqual(capture_output(2)[1].split(), ["2","2","2","10"])
 
if __name__ == '__main__':
    unittest.main()