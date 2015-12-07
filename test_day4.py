import unittest
from algorithms import Md5Solver


class test_day4(unittest.TestCase):
    def setUp(self):
        self.solver = Md5Solver()

    def test_whenKeyIsabcdef609043TheAnswerStartsWithFiveZeros(self):
        key = "abcdef609043"
        string = self.solver.get_md5(key)
        self.assertEqual(True, self.solver.string_starts_with_n_zeros(string, 5))

    def test_whenKeyIsblahThenAnswerStartsWithFveZeros(self):
        key = "pqrstuv1048970"
        string = self.solver.get_md5(key)
        self.assertEqual(True, self.solver.string_starts_with_n_zeros(string, 5))

    def test_whenSecretKeyIsabcdefThenResultIs609043(self):
        self.assertEqual(self.solver.solve("abcdef", 5), "609043")

    def test_whenSecretKeyIspqrstuvThenResultIs1048970(self):
        self.assertEqual(self.solver.solve("pqrstuv", 5), "1048970")