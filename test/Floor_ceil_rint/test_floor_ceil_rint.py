import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Floor_ceil_rint")))
from util import floor_ceil_rint

class TestFloorCeilRint(unittest.TestCase):

    def test_positive_floats(self):
        arr = np.array([1.1, 2.2, 3.3])
        floor, ceil, rint = floor_ceil_rint(arr)
        np.testing.assert_array_equal(floor, [1., 2., 3.])
        np.testing.assert_array_equal(ceil,  [2., 3., 4.])
        np.testing.assert_array_equal(rint,  [1., 2., 3.])

if __name__ == "__main__":
    unittest.main(verbosity=2)