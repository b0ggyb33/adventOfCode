import unittest
from algorithms import countLineCharacters
class test_day8(unittest.TestCase):

    def test_twoquotesreturnszero(self):
        self.assertEqual((2,0),countLineCharacters(r""))

    def test_abcReturns5_3(self):
        self.assertEqual((5,3),countLineCharacters(r"abc"))

    def test_aaaquoteaaa_returns_10_7(self):
        self.assertEqual((10,7),countLineCharacters(r"aaa\"aaa"))

    def test_hex27_returns6_1(self):
        self.assertEqual((6,1),countLineCharacters(r"\x27"))

    def test_doubleescape(self):
        self.assertEqual((10,7),countLineCharacters(r"aaa\\aaa"))

    def test_difficultCase(self):
        self.assertEqual((33,27),countLineCharacters(r"rq\\\"mohnjdf\\xv\\hrnosdtmvxot"))

    def test_sample(self):
        lines=[line for line in open("testData/stringLiterals")]
        for line in lines[:1]:
            self.assertEqual((24,22),countLineCharacters(line.strip("\"\n")))
        charCount=0
        dataCount=0
        for line in lines[:2]:
            chars,data = countLineCharacters(line.strip("\"\n"))
            charCount+=chars
            dataCount+=data
        self.assertEqual((24+28,22+18),(charCount,dataCount))

    def test_example(self):
        charCount,dataCount=0,0
        lines=[r"",r"abc",r"aaa\"aaa",r"\x27"]
        for line in lines:
            chars,data = countLineCharacters(line)
            charCount+=chars
            dataCount+=data
        self.assertEqual(12,charCount-dataCount)

    def test_fullSample(self):
        lines=[line for line in open("testData/stringLiterals")]
        charCount=0
        dataCount=0
        for line in lines:
            chars,data = countLineCharacters(line.strip("\"\n\"" ))
            charCount+=chars
            dataCount+=data
        print charCount-dataCount
        self.assertGreater(charCount-dataCount,1329)