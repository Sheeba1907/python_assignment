import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Linear_algebra")))
from util import determinant

class TestMatrixDeterminant(unittest.TestCase):

    def test_matrix_determinant_1(self):
        matrix = np.array([[1.1, 1.1],
                           [1.1, 1.1]])
        self.assertEqual(determinant(matrix), 0.0)

    def test_matrix_determinant_2(self):
        matrix = np.array([[1, 0],
                           [0, 1]])
        self.assertEqual(determinant(matrix), 1.0)

    def test_matrix_determinant_3(self):
        matrix = np.array([[2, 4, 2],
                           [1, 2, 1],
                           [3, 6, 3]])
        # Rows are linearly dependent → determinant = 0
        self.assertEqual(determinant(matrix), 0.0)

    def test_matrix_determinant_4(self):
        matrix = np.array([[1, -2],
                           [-3, 4]])
        # Determinant = 1*4 - (-2*-3) = 4 - 6 = -2
        self.assertEqual(determinant(matrix), -2.0)

if __name__ == "__main__":
    unittest.main()