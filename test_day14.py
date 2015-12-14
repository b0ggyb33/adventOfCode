import unittest
from algorithms import Reindeer
class test_day14(unittest.TestCase):

    def setUp(self):
        self.reindeer = Reindeer(speed=10,rest_time=20,rest_length=1)

    def moveReindeer(self,time):
        self.reindeer.fly(time)
        return self.reindeer.distance

    def test_ReindeerFlys_10m_in_1s(self):
        self.assertEqual(10,self.moveReindeer(1))

    def test_ReindeerFlys_100m_in_10s(self):
        self.assertEqual(100,self.moveReindeer(10))

    def test_reindeerHasARestAfter20sFor1s(self):
        self.assertEqual(200,self.moveReindeer(21))

    def test_reindeerHasARestAfter20sFor1sThenFlysAgain(self):
        self.assertEqual(210,self.moveReindeer(22))

    def test_reindeerHasHadTwoRestsAfter44s(self):
        self.assertEqual(420,self.moveReindeer(44))

    def test_rudolphHasGoneFurtherThanSelf(self):
        rudolph = Reindeer(10,rest_time=30,rest_length=1)
        self.moveReindeer(50)
        rudolph.fly(50)
        self.assertEqual(True,rudolph>self.reindeer)