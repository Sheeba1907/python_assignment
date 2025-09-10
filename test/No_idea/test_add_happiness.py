import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/No_idea")))
from util import add_happiness

class TestAddHappiness(unittest.TestCase):

    def test_add_happiness_1(self):
        array = [1, 5, 3]
        set_like = {3, 1}
        set_dislike = {5, 7}
        self.assertEqual(add_happiness(array, set_like, set_dislike), 1)

    def test_add_happiness_2(self):
        array = [1, 2, 3]
        set_like = {1, 2, 3}
        set_dislike = {4, 5}
        self.assertEqual(add_happiness(array, set_like, set_dislike), 3)

    def test_add_happiness_3(self):
        array = [1, 2, 3]
        set_like = {4, 5}
        set_dislike = {1, 2, 3}
        self.assertEqual(add_happiness(array, set_like, set_dislike), -3)

    def test_add_happiness_4(self):
        array = [1, 2, 2, 3, 4]
        set_like = {2, 3}
        set_dislike = {4, 5}
        # +1 for 2 (twice) = +2, +1 for 3 = +1, -1 for 4 = -1 → total 2
        self.assertEqual(add_happiness(array, set_like, set_dislike), 2)

    def test_add_happiness_5(self):
        array = [1, 2, 3]
        set_like = {4, 5}
        set_dislike = {6, 7}
        self.assertEqual(add_happiness(array, set_like, set_dislike), 0)

if __name__ == "__main__":
    unittest.main()