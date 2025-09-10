import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Collections")))
from util import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_case_1(self):
        n = 5
        headers = ["ID", "MARKS", "NAME", "CLASS"]
        rows = [
            ["1", "97", "Raymond", "7"],
            ["2", "50", "Steven", "4"],
            ["3", "91", "Adrian", "9"],
            ["4", "72", "Stewart", "5"],
            ["5", "80", "Peter", "6"],
        ]
        result = calculate_average(n, headers, rows)
        self.assertAlmostEqual(result, 78.00, places=2)

    def test_case_2(self):
        n = 5
        headers = ["MARKS", "CLASS", "NAME", "ID"]
        rows = [
            ["92", "2", "Calum", "1"],
            ["82", "5", "Scott", "2"],
            ["94", "2", "Jason", "3"],
            ["55", "8", "Glenn", "4"],
            ["82", "2", "Fergus", "5"],
        ]
        result = calculate_average(n, headers, rows)
        self.assertAlmostEqual(result, 81.00, places=2)

    def test_case_3(self):
        n = 1
        headers = ["NAME", "CLASS", "MARKS", "ID"]
        rows = [
            ["Alice", "10", "88", "1"]
        ]
        result = calculate_average(n, headers, rows)
        self.assertEqual(result, 88.00)

    def test_case_4(self):
        n = 3
        headers = ["CLASS", "ID", "MARKS", "NAME"]
        rows = [
            ["5", "1", "100", "Tom"],
            ["6", "2", "50", "Jerry"],
            ["7", "3", "70", "Mickey"],
        ]
        result = calculate_average(n, headers, rows)
        self.assertAlmostEqual(result, 73.33, places=2)

if __name__ == "__main__":
    unittest.main()