import unittest
from algorithms import Wire
class test_day7(unittest.TestCase):
    def test_wireholdsvalue(self):
        wire=Wire()
        self.assertEqual(0,wire)

    def test_canSetValue(self):
        wire=Wire(10)
        self.assertEqual(10,wire)

    def test_ANDwithtwowires(self):
        a=Wire(1)
        b=Wire(0)
        self.assertEqual(0,a & b)

    def test_ORwithTwowires(self):
        a=Wire(5)
        b=Wire(2)
        self.assertEqual(7,a | b)