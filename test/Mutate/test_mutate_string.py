import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Mutate")))
from util import mutate_string

class TestMutateString(unittest.TestCase):
 
    def test_mutate_string_1(self):
        self.assertEqual(mutate_string("abracadabra", 5, "k"), "abrackdabra")
    def test_mutate_string_2(self):
        self.assertEqual(mutate_string("hello", 0, "H"), "Hello")
    def test_mutate_string_3(self):
        self.assertEqual(mutate_string("python", 5, "X"), "pythoX")
    def test_mutate_string_4(self):
        self.assertEqual(mutate_string("world", 2, "R"), "woRld") 
 
if __name__ == '__main__':
    unittest.main()