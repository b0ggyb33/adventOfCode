import unittest
from algorithms import Reindeer
class test_day14(unittest.TestCase):

    def setUp(self):
        self.reindeer = Reindeer(name="bob",speed=10,rest_time=20,rest_length=1)
        self.reindeerList = self.loadTestData()

    def loadTestData(self):
        lines=[line for line in open("testData/reindeerRacing")]
        reindeer=[]
        for line in lines:
            name,gumf=line.split("can fly ")
            speed,gumf=gumf.split("km/s for ")
            rest_time,gumf=gumf.split("seconds, but then must rest for ")
            rest_duration,_=gumf.split("seconds")
            reindeer.append(Reindeer(name,int(speed),int(rest_time),int(rest_duration)))
        return reindeer

    def moveReindeer(self,reindeer,time):
        reindeer.fly(time)
        return reindeer.distance

    def test_ReindeerFlys_10m_in_1s(self):
        self.assertEqual(10,self.moveReindeer(self.reindeer,1))

    def test_ReindeerFlys_100m_in_10s(self):
        self.assertEqual(100,self.moveReindeer(self.reindeer,10))

    def test_reindeerHasARestAfter20sFor1s(self):
        self.assertEqual(200,self.moveReindeer(self.reindeer,21))

    def test_reindeerHasARestAfter20sFor1sThenFlysAgain(self):
        self.assertEqual(210,self.moveReindeer(self.reindeer,22))

    def test_reindeerHasHadTwoRestsAfter44s(self):
        self.assertEqual(420,self.moveReindeer(self.reindeer,44))

    def test_rudolphHasGoneFurtherThanSelf(self):
        rudolph = Reindeer("rudolph",10,rest_time=30,rest_length=1)
        self.moveReindeer(self.reindeer,50)
        self.moveReindeer(rudolph,50)
        self.assertEqual(490,rudolph.distance)
        self.assertEqual(True,rudolph.distance>self.reindeer.distance)

    def test_brokenExample(self):
        rudolph = Reindeer("rudolph",10,20,100)
        self.moveReindeer(rudolph,100)
        self.assertEqual(200,rudolph.distance)

    def testCometexample(self):
        comet = Reindeer("comet",14,10,127)
        self.moveReindeer(comet,1000)
        self.assertEqual(1120,comet.distance)

    def testDancerexample(self):
        dancer = Reindeer("dancer",16,11,162)
        self.moveReindeer(dancer,1000)
        self.assertEqual(1056,dancer.distance)

    def test_cometFurtherThanDancer(self):
        comet = Reindeer("comet",14,10,127)
        dancer = Reindeer("dancer",16,11,162)
        self.moveReindeer(comet,1000)
        self.moveReindeer(dancer,1000)

        self.assertEqual(True,comet.distance>dancer.distance)

    def test_part1(self):
        [rein.fly(2503) for rein in self.reindeerList]
        print max([reindo.distance for reindo in self.reindeerList])

