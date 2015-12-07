import unittest
from algorithms import get_houses_visited
class test_day3(unittest.TestCase):
    def test_whenGivenLTThenReturnTwo(self):
        self.assertEqual(2,get_houses_visited(">"))

    def test_whenGivenUpDownThenReturnThree(self):
        self.assertEqual(3,get_houses_visited("^v"))

    def test_whenVisitingFuorHousesInaGridThenReturn4(self):
        self.assertEqual(3,get_houses_visited("^>v<"))

    def test_whengivenupdownetcthenreturn2(self):
        self.assertEqual(11,get_houses_visited("^v^v^v^v^v"))