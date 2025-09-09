import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Merge")))
from util import merge_tools

class TestMergeTools(unittest.TestCase):
 
    def test_merge_tools_1(self):
        self.assertEqual(merge_tools("AABCAAADA",3), ["AB","CA","AD"])
    def test_merge_tools_2(self):
        self.assertEqual(merge_tools("ABCDEFGH",2), ["AB","CD","EF","GH"])
    def test_merge_tools_3(self):
        self.assertEqual(merge_tools("AAABBBCCC",3), ["A","B","C"])
    def test_merge_tools_4(self):
        self.assertEqual(merge_tools("ABCDE",1), ["A","B","C","D","E"]) 
    def test_merge_tools_5(self):
        self.assertEqual(merge_tools("AABBCC",6), ["ABC"]) 
 
if __name__ == '__main__':
    unittest.main()