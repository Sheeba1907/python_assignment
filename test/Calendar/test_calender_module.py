import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Calendar")))
from util import calendar_module

class TestCalenderModule(unittest.TestCase):
    def test_calendar_module1(self):
        self.assertEqual(calendar_module(8, 5, 2015), "WEDNESDAY")
    def test_calendar_module2(self):
        self.assertEqual(calendar_module(1, 1, 2000), "SATURDAY")
    def test_calendar_module3(self):
        self.assertEqual(calendar_module(12, 25, 2020), "FRIDAY")
    def test_calendar_module4(self):
        self.assertEqual(calendar_module(2, 29, 2016), "MONDAY")
    def test_calendar_module5(self):
        self.assertEqual(calendar_module(12, 31, 1999), "FRIDAY")
 
if __name__ == '__main__':
    unittest.main()