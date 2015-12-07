import unittest
from algorithms import get_floor
class test_day1(unittest.TestCase):
    def test_whenGivenOpenParenthesisIncreaseFloor(self):
        self.assertEqual(1,get_floor("("))

    def test_whenGivenClosedParenthesisDecreaseFloor(self):
        self.assertEqual(-1,get_floor(")"))

    def test_whenInputisTwoParenthesisPairsOutputIsZero(self):
        self.assertEqual(0,get_floor("(())"))

    def test_whenInputIsOneUnopenedClosedBrackerOutputisNegative(self):
        self.assertEqual(-1,get_floor("())"))

    def test_getCharacterOfBasementIsOneGivenClosedParenthesis(self):
        self.assertEqual(1,get_floor(")",return_basement_index=True)[1])

    def test_getCharacterOfbasementIsFiveGivenExample(self):
        example="()())"
        self.assertEqual(5,get_floor(example,return_basement_index=True)[1])