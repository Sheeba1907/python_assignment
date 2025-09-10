import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Min_max")))
from util import minmax

class TestMinMax(unittest.TestCase):

    def test_min_max_1(self):
        arr = np.array([
            [2, 5],
            [3, 7],
            [1, 3],
            [4, 0]
        ])
        self.assertEqual(minmax(arr), 3)

    def test_min_max_2(self):
        arr = np.array([
            [5, 1, 9],
            [2, 8, 3],
            [4, 6, 7]
        ])
        # Row minima: [1,2,4] → max = 4
        self.assertEqual(minmax(arr), 4)

    def test_min_max_3(self):
        arr = np.array([
            [10, 20, 30, 5],
            [1, 2, 3, 4],
            [7, 8, 9, 6]
        ])
        # Row minima: [5,1,6] → max = 6
        self.assertEqual(minmax(arr), 6)

    def test_min_max_4(self):
        arr = np.array([
            [-3, -1, -7],
            [-5, -2, -4],
            [-6, -8, -9]
        ])
        self.assertEqual(minmax(arr), -5)

if __name__ == "__main__":
    unittest.main()