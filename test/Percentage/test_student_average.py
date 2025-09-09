import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Percentage")))
from util import student_average

class TestStudentAverage(unittest.TestCase):
 
    def test_student_average_1(self):
        self.assertEqual(student_average('alpha', 10, 20, 30), 20.00)
    def test_student_average_2(self):
        self.assertEqual(student_average('beta', 40, 50, 60), 50.00)
    def test_student_average_3(self):
        self.assertEqual(student_average('gamma', 70, 80, 90), 80.00)
    def test_student_average_4(self):
        self.assertEqual(student_average('delta', 10, 40, 80), 43.33)  
 
if __name__ == '__main__':
    unittest.main()