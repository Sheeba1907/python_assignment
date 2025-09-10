import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Time_delta")))
from util import time_difference

class TestTimeDifference(unittest.TestCase):

    def test_time_difference_1(self):
        t1 = "Sun 10 May 2015 13:54:36 +0000"
        t2 = "Sun 10 May 2015 13:54:36 +0000"
        self.assertEqual(time_difference(t1, t2), 0)

    def test_time_difference_2(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_difference(t1, t2), 25200)  # 7 hours = 25200 seconds

    def test_time_difference_3(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(time_difference(t1, t2), 88200)

    def test_time_difference_4(self):
        t1 = "Thu 31 Dec 2020 23:59:59 +0000"
        t2 = "Fri 01 Jan 2021 00:00:59 +0000"
        self.assertEqual(time_difference(t1, t2), 60)

    def test_time_difference_5(self):
        t1 = "Mon 01 Mar 2021 10:00:00 -0500"  
        t2 = "Mon 01 Mar 2021 10:00:00 +0000"  
        self.assertEqual(time_difference(t1, t2), 18000)  

if __name__ == "__main__":
    unittest.main()