import unittest
from algorithms import get_wrapping_volume
class test_day2(unittest.TestCase):
    def test_given2x3x4thenreturnis58(self):
        self.assertEqual((58,34),get_wrapping_volume("2x3x4"))

    def test_given1x1x10thenreturn43(self):
        self.assertEqual((43,14),get_wrapping_volume("1x1x10"))