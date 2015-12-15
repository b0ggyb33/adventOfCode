import unittest
from algorithms import countLineCharacters, processStringLiterals
class test_day8(unittest.TestCase):

    def setUp(self):
        self.testData = [line for line in open("testData/stringLiterals")]

    def test_twoquotesreturnszero(self):
        self.assertEqual((2,0),countLineCharacters(r""))

    def test_twoquotesreturnszerowhenwrittenasintest(self):
        self.assertEqual(2,processStringLiterals(["\"\"\n"]))

    def test_abcReturns5_3(self):
        self.assertEqual((5,3),countLineCharacters(r"abc"))

    def test_aaaquoteaaa_returns_10_7(self):
        self.assertEqual((10,7),countLineCharacters(r"aaa\"aaa"))

    def test_hex27_returns6_1(self):
        self.assertEqual((6,1),countLineCharacters(r"\x27"))

    def test_double_escape(self):
        self.assertEqual((10,7),countLineCharacters(r"aaa\\aaa"))

    def test_difficultCase(self):
        self.assertEqual((33,27),countLineCharacters(r"rq\\\"mohnjdf\\xv\\hrnosdtmvxot"))

    def test_example(self):
        lines=[r"",r"abc",r"aaa\"aaa",r"\x27"]
        self.assertEqual(12,processStringLiterals(lines))

    def test_sample1(self):
        self.assertEqual(2,processStringLiterals(self.testData[:1]))

    def test_sample_first2(self):
        self.assertEqual((24+28)-(22+18),processStringLiterals(self.testData[:2]))

    def test_sample4(self):
        self.assertEqual(23-18,processStringLiterals(self.testData[4:5]))

    def test_sample_line59(self):
        self.assertEqual(2,processStringLiterals(self.testData[58:59]))

    def test_sample_line87(self):
        self.assertEqual(14-8,processStringLiterals(self.testData[86:87]))

    def test_fullSample(self):
        self.assertEqual(processStringLiterals(self.testData),1342)