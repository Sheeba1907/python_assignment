import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Valid_email")))
from util import filter_mails

class TestValidateEmail(unittest.TestCase):

    def test_validate_email_1(self):
        emails = [
            "lara@hackerrank.com",
            "brian-23@hackerrank.com",
            "britts_54@hackerrank.com"
        ]
        expected = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
        self.assertEqual(filter_mails(emails), expected)

    def test_validate_email_2(self):
        emails = [
            "lar*a@hackerrank.com",
            "brian-23@hackerrank.com"
        ]
        expected = ["brian-23@hackerrank.com"]
        self.assertEqual(filter_mails(emails), expected)

    def test_validate_email_3(self):
        emails = [
            "lara@hackerrank.comm",
            "brian@hackerrank.com"
        ]
        expected = ["brian@hackerrank.com"]
        self.assertEqual(filter_mails(emails), expected)

    def test_validate_email_4(self):
        emails = []
        expected = []
        self.assertEqual(filter_mails(emails), expected)

    def test_validate_email_5(self):
        emails = [
            "lara@hackerrank.comm1",
            "brian@@hackerrank.com",
            "b@h.c0m"
        ]
        expected = []
        self.assertEqual(filter_mails(emails), expected)


if __name__ == "__main__":
    unittest.main()