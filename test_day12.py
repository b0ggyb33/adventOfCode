import unittest
import json


def find_all_the_numbers(test_input, ignore_red=False):

    json_sum = 0

    if type(test_input) == dict:
        local_sum = 0
        for value in test_input.values():
            if ignore_red and value == "red":
                local_sum = 0
                break
            else:
                local_sum += find_all_the_numbers(value, ignore_red)
        json_sum += local_sum
    elif type(test_input) == list:
        for value in test_input:
            json_sum += find_all_the_numbers(value, ignore_red)
    elif type(test_input) == int:
        json_sum += test_input

    return json_sum


class TestDay12(unittest.TestCase):

    def testWorksWithJustAnInt(self):
        self.assertEqual(find_all_the_numbers(7), 7)

    def testWorksWithAString(self):
        self.assertEqual(find_all_the_numbers("7"), 0)

    def testCanReadFromFlatJson(self):
        test_input = {'a': 0, 'b': 1, 'c': 2}
        self.assertEqual(find_all_the_numbers(test_input), 3)

    def testCanReadFromJsonWithAList(self):
        test_input = {'a': [0, 2, 3], 'b': 1, 'c': 2}
        self.assertEqual(find_all_the_numbers(test_input), 8)

    def testCanReadFromANestedList(self):
        test_input = {'a': [[0, 2, 3]], 'b': 1, 'c': 2}
        self.assertEqual(find_all_the_numbers(test_input), 8)

    def testExamples(self):
        self.assertEqual(find_all_the_numbers({"a": {"b": 4}, "c": -1}), 3)
        self.assertEqual(find_all_the_numbers([[[3]]]), 3)
        self.assertEqual(find_all_the_numbers([1, 2, 3]), 6)
        self.assertEqual(find_all_the_numbers({"a": 2, "b": 4}), 6)
        self.assertEqual(find_all_the_numbers([]), 0)
        self.assertEqual(find_all_the_numbers({}), 0)

    def testPartOne(self):
        test_input = json.load(open("testData/numbers.json"))
        self.assertEqual(find_all_the_numbers(test_input), 156366)

    def test_forRedInDict(self):
        test_input = [1, {"c": "red", "b": 2}, 3]
        self.assertEqual(find_all_the_numbers(test_input, ignore_red=True), 4)

    def test_forRedInWholeJson(self):
        test_input = {"d": "red", "e": [1, 2, 3, 4], "f": 5}
        self.assertEqual(find_all_the_numbers(test_input, ignore_red=True), 0)

    def test_forRedInListIsUnaffected(self):
        test_input = [1, "red", 5]
        self.assertEqual(find_all_the_numbers(test_input, ignore_red=True), 6)

    def testPartTwo(self):
        test_input = json.load(open("testData/numbers.json"))
        self.assertEqual(find_all_the_numbers(test_input, ignore_red=True), 96852)
