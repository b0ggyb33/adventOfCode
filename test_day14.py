import unittest
from algorithms import Reindeer
class test_day14(unittest.TestCase):

    def setUp(self):
        self.reindeer = Reindeer(name="bob",speed=10,rest_time=20,rest_length=1)
        self.reindeerList = self.loadTestData()
        self.comet = Reindeer("comet",14,10,127)
        self.dancer = Reindeer("dancer",16,11,162)
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

    def test_ReindeerFlies_100m_in_10s_inTen_Calls(self):
        for i in range(10):
            self.moveReindeer(self.reindeer,1)

        self.assertEqual(100,self.reindeer.distance)

    def test_reindeerHasARestAfter20sFor1s(self):
        self.assertEqual(200,self.moveReindeer(self.reindeer,21))
        self.assertEqual(True,self.reindeer.resting)

    def test_reindeerHasARestAfter20sFor1sThenFlysAgain(self):
        for i in xrange(22):
            self.moveReindeer(self.reindeer,1)
        self.assertEqual(210,self.reindeer.distance)

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
        self.moveReindeer(self.comet,1000)
        self.assertEqual(1120,self.comet.distance)

    def testDancerexample(self):
        self.moveReindeer(self.dancer,1000)
        self.assertEqual(1056,self.dancer.distance)

    def test_cometFurtherThanDancer(self):
        self.moveReindeer(self.comet,1000)
        self.moveReindeer(self.dancer,1000)
        self.assertEqual(True,self.comet.distance>self.dancer.distance)

    def test_part1(self):
        [rein.fly(2503) for rein in self.reindeerList]
        self.assertEqual(2696, max([reindo.distance for reindo in self.reindeerList]))

    def test_oneSecondGiveOutStar(self):
        [reindeer.fly(1) for reindeer in self.reindeerList]
        self.assertEqual((25,"Donner"), max([(reindo.distance,reindo.name) for reindo in self.reindeerList]))
        _,fastestReindeer = max([(reindeer.distance,reindeer) for reindeer in self.reindeerList])
        fastestReindeer.awardStar()
        self.assertEqual((1,"Donner"), max([(reindo.stars,reindo.name) for reindo in self.reindeerList]))

    def testFakeReindeer(self):
        reindeerList=[Reindeer("bob",10,1,1),Reindeer("fred",8,10,1)]
        for idx in range(3):
            [reindeer.fly(1) for reindeer in reindeerList]
            _,fastestReindeer = max([(reindeer.distance,reindeer) for reindeer in reindeerList])
            fastestReindeer.awardStar()
        self.assertEqual((2,"fred"), max([(reindo.stars,reindo.name) for reindo in reindeerList]))

    def test_comet_dancer_example_2(self):
        reindeerList=[self.dancer,self.comet]
        for idx in range(1000):
            [reindeer.fly(1) for reindeer in reindeerList]
            maxDistance=0
            for reindeer in reindeerList:
                if reindeer.distance>maxDistance:
                    maxDistance=reindeer.distance

            for reindeer in reindeerList:
                if reindeer.distance==maxDistance:
                    reindeer.awardStar()
        self.assertEqual(689,self.dancer.stars)
        self.assertEqual(312,self.comet.stars)

    def test_part2(self):
        for idx in range(2503):
            [reindeer.fly(1) for reindeer in self.reindeerList]
            maxDistance=0
            for reindeer in self.reindeerList:
                if reindeer.distance>maxDistance:
                    maxDistance=reindeer.distance

            for reindeer in self.reindeerList:
                if reindeer.distance==maxDistance:
                    reindeer.awardStar()

        maxstars,maxname = max([(reindo.stars,reindo.name) for reindo in self.reindeerList])
        self.assertEqual(maxstars,1084)