import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Runner_up")))
from util import runner_up_score

class TestStudentAverage(unittest.TestCase):
 
    def test_runner_up_score_1(self):
        self.assertEqual(runner_up_score([2, 3, 6, 6, 5]), 5)
    def test_runner_up_score_2(self):
        self.assertEqual(runner_up_score([10, 10, 9, 8]), 9)
    def test_runner_up_score_3(self):
        self.assertEqual(runner_up_score([100, 50, 25, 10, 5]), 50)
    def test_runner_up_score_4(self):
        self.assertEqual(runner_up_score([1, 2, 3, 4, 5]), 4) 
 
if __name__ == '__main__':
    unittest.main()