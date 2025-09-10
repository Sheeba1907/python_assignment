import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Word_order")))
from util import count_distinct_words

class TestCountWords(unittest.TestCase):

    def test_count_distinct_words_1(self):
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]
        distinct, counts = count_distinct_words(words)
        self.assertEqual(distinct, 3)
        self.assertEqual(counts, [2, 1, 1])

    def test_count_distinct_words_2(self):
        words = ["apple", "banana", "cherry"]
        distinct, counts = count_distinct_words(words)
        self.assertEqual(distinct, 3)
        self.assertEqual(counts, [1, 1, 1])

    def test_count_distinct_words_3(self):
        words = ["word", "word", "word", "word"]
        distinct, counts = count_distinct_words(words)
        self.assertEqual(distinct, 1)
        self.assertEqual(counts, [4])

    def test_count_distinct_words_4(self):
        words = ["cat", "dog", "cat", "bird", "dog", "dog"]
        distinct, counts = count_distinct_words(words)
        self.assertEqual(distinct, 3)
        self.assertEqual(counts, [2, 3, 1])  


if __name__ == "__main__":
    unittest.main()