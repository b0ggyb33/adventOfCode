import unittest
import collections
import itertools
import operator

def parseString(string):
    destinations, distance = string.split(" = ")
    origin, destination = destinations.split(" to ")
    return [origin, destination, int(distance)]


def addDistance(distances,string):
    origin, destination, distance = parseString(string)
    distances[origin][destination]=distance
    distances[destination][origin] = distance


def getShortestRoute(distances):
    return getRoute(distances, shortest=True)

def getRoute(distances, shortest=True):
    if shortest:
        useThisOperator=operator.le
        distance=float('inf')
    else:
        useThisOperator = operator.ge
        distance=0

    for permutation in itertools.permutations(distances.keys()):
        localDistance = 0
        for index,place in enumerate(permutation[:-1]):
            localDistance += distances[permutation[index-1]][permutation[index]]
        if useThisOperator(localDistance,distance):
            distance=localDistance
    return distance

def getLongestRoute(distances):
    return getRoute(distances,shortest=False)


class TestDay9(unittest.TestCase):
    def setUp(self):
        self.testString = "London to Dublin = 464"
    def testCanParseString(self):

        data = parseString(self.testString)
        self.assertEqual(data,["London", "Dublin", 464])

    def testCanPutValueInDict(self):
        data = collections.defaultdict(dict)
        addDistance(data,self.testString)
        self.assertEqual(data["London"]["Dublin"], 464)

    def test_distancesAreReversibled(self):
        data = collections.defaultdict(dict)
        addDistance(data, self.testString)
        self.assertEqual(data["Dublin"]["London"], 464)

    def test_shortestRoute(self):
        data = collections.defaultdict(dict)
        addDistance(data, "London to Dublin = 464")
        addDistance(data, "London to Belfast = 518")
        addDistance(data, "Dublin to Belfast = 141")

        self.assertEqual(getShortestRoute(data),605)

    def test_PartOne(self):
        data=open("testData/distancesDay9.txt")
        distances = collections.defaultdict(dict)
        for line in data.readlines():
            line=line.rstrip("\n")
            addDistance(distances, line)

        self.assertEqual(getShortestRoute(distances), 251)

    def test_longestRoute(self):
        data = collections.defaultdict(dict)
        addDistance(data, "London to Dublin = 464")
        addDistance(data, "London to Belfast = 518")
        addDistance(data, "Dublin to Belfast = 141")

        self.assertEqual(getLongestRoute(data), 982)

    def test_PartTwo(self):
        data = open("testData/distancesDay9.txt")
        distances = collections.defaultdict(dict)
        for line in data.readlines():
            line = line.rstrip("\n")
            addDistance(distances, line)

        self.assertEqual(getLongestRoute(distances), 898)