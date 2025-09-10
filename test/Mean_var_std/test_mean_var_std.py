import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Mean_var_std")))
from util import mean_var_std

class TestMeanVarStd(unittest.TestCase):

    def test_mean_var_std_1(self):
        arr = np.array([[1, 2],
                        [3, 4]])
        mean, var, std = mean_var_std(arr)
        np.testing.assert_array_almost_equal(mean, [1.5, 3.5])
        np.testing.assert_array_almost_equal(var, [1.0, 1.0])
        self.assertAlmostEqual(std, 1.11803398875, places=8)

    def test_mean_var_std_2(self):
        arr = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
        mean, var, std = mean_var_std(arr)
        np.testing.assert_array_almost_equal(mean, [2.0, 5.0, 8.0])
        np.testing.assert_array_almost_equal(var, [6.0, 6.0, 6.0])
        self.assertAlmostEqual(std, np.std(arr), places=8)

    def test_mean_var_std_3(self):
        arr = np.array([[-1, -2],
                        [-3, -4]])
        mean, var, std = mean_var_std(arr)
        np.testing.assert_array_almost_equal(mean, [-1.5, -3.5])
        np.testing.assert_array_almost_equal(var, [1.0, 1.0])
        self.assertAlmostEqual(std, 1.11803398875, places=8)

    def test_mean_var_std_4(self):
        arr = np.array([[1, 2, 3],
                        [4, 5, 6]])
        mean, var, std = mean_var_std(arr)
        np.testing.assert_array_almost_equal(mean, [2.0, 5.0])
        np.testing.assert_array_almost_equal(var, [2.25, 2.25, 2.25])
        self.assertAlmostEqual(std, np.std(arr), places=8)

if __name__ == "__main__":
    unittest.main()