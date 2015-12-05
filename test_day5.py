import unittest
from algorithms import NiceStringFinder


class test_day5(unittest.TestCase):

    def setUp(self):
        self.stringFinder=NiceStringFinder()

    def three_vowels(self,string):
        return self.stringFinder.contains_three_vowels(string)

    def double_letter(self,string):
        return self.stringFinder.contains_double_letter(string)

    def naughty_substring(self,string):
        return self.stringFinder.contains_naughty_substring(string)

    def isNice(self,string):
        return self.stringFinder.isNice(string)

    def doublePair(self,string):
        return self.stringFinder.containsADoublePair(string)

    def sandwich(self,string):
        return self.stringFinder.contains_sandwich(string)

    def isNice2(self,string):
        return self.stringFinder.isNicePart2(string)

    def test_abcdefghi_containsthreevowels(self):
        string="abcdefghi"
        self.assertEqual(True,self.three_vowels(string))

    def test_abcdde_ContainsOneDoubleLetter(self):
        string='abcdde'
        self.assertEqual(True,self.double_letter(string))

    def test_xzacef_DoesNotContainNaughtySubstring(self):
        string='xzacef'
        self.assertEqual(False,self.naughty_substring(string))

    def test_xzabcef_ContainsNaughtySubstring(self):
        string='xzabcef'
        self.assertEqual(True,self.naughty_substring(string))

    def test_ugknbfddgicrmopn_isNice(self):
        string="ugknbfddgicrmopn"
        self.assertEqual(True,self.isNice(string))

    def test_aaa_isNice(self):
        string="aaa"
        self.assertEqual(True,self.three_vowels(string))
        self.assertEqual(True,self.isNice(string))

    def test_jchzalrnumimnmhp_isNaughty(self):
        string="jchzalrnumimnmhp"
        self.assertEqual(False,self.isNice(string))

    def test_haegwjzuvuyypxyu_isNaughty(self):
        string="haegwjzuvuyypxyu"
        self.assertEqual(False,self.isNice(string))

    def test_dvszwmarrgswjxmb_isNaughty(self):
        string="dvszwmarrgswjxmb"
        self.assertEqual(False,self.isNice(string))

    def test_using_input_output_is_255_for_part_one(self):
        self.assertEqual(255,sum([self.isNice(string.strip("\n")) for string in open("niceStrings")]))


    def test_aaa_isNaughty(self):
        self.assertEqual(False,self.doublePair("aaa"))

    def test_xyxy_isNice(self):
        self.assertEqual(True,self.doublePair("xyxy"))

    def test_aabcdefgaa_isNice(self):
        self.assertEqual(True,self.doublePair("aabcdefgaa"))

    def test_bcdefgaa_isNaughty(self):
        self.assertEqual(False,self.doublePair("bcdefgaa"))

    def test_abcdefeghi_containsSandwich(self):
        self.assertEqual(True,self.sandwich("abcdefeghi"))

    def test_abcdefgh_doesNotContainSandwich(self):
        self.assertEqual(False,self.sandwich("abcdefgh"))

    def test_qjhvhtzxzqqjkmpb_isNice(self):
        self.assertEqual(True,self.isNice2("qjhvhtzxzqqjkmpb"))

    def test_xxyxx_isNice(self):
        self.assertEqual(True,self.isNice2("xxyxx"))

    def test_uurcxstgmygtbstg_isNaughty(self):
        self.assertEqual(False,self.isNice2("uurcxstgmygtbstg"))

    def test_ieodomkazucvgmuy_isNaughty(self):
        self.assertEqual(False,self.isNice2("ieodomkazucvgmuy"))

    def test_using_input_output_is_55_for_part_two(self):
        self.assertEqual(55,sum([self.isNice2(string.strip("\n")) for string in open("niceStrings")]))
