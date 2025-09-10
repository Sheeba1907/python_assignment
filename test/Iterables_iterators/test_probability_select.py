import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Iterables_iterators")))
from util import probability_select

class TestProbabilitySelected(unittest.TestCase):

    def test_probability_select_1(self):
        arr = ['a', 'a', 'c', 'd']
        k = 2
        self.assertAlmostEqual(probability_select(arr, k), 0.8333, places=4)

    def test_probability_select_2(self):
        arr = ['a', 'a', 'a', 'a']
        k = 2
        self.assertAlmostEqual(probability_select(arr, k), 1.0, places=4)

    def test_probability_select_3(self):
        arr = ['b', 'c', 'd']
        k = 2
        self.assertAlmostEqual(probability_select(arr, k), 0.0, places=4)

    def test_probability_select_4(self):
        arr = ['a', 'b', 'c']
        k = 3
        self.assertAlmostEqual(probability_select(arr, k), 1.0, places=4)

    def test_probability_select_5(self):
        arr = ['a', 'b', 'c']
        k = 4
        self.assertAlmostEqual(probability_select(arr, k), 0.0, places=4)

if __name__ == "__main__":
    unittest.main()