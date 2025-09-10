import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Piling_up")))
from util import stack_cubes

class TestStackCubes(unittest.TestCase):

    def test_stack_cubes_1(self):
        self.assertEqual(stack_cubes([4, 3, 2, 1, 3, 4]), "Yes")
        self.assertEqual(stack_cubes([1, 3, 2]), "No")

    def test_stack_cubes_2(self):
        self.assertEqual(stack_cubes([5, 4, 3, 2, 1]), "Yes")

    def test_stack_cubes_3(self):
        self.assertEqual(stack_cubes([1, 2, 3, 4, 5]), "Yes")

    def test_stack_cubes_4(self):
        self.assertEqual(stack_cubes([2, 2, 2, 2]), "Yes")

    def test_stack_cubes_5(self):
        # Peak in the middle cannot form valid pile
        self.assertEqual(stack_cubes([1, 3, 5, 4, 2]), "No")

if __name__ == "__main__":
    unittest.main()