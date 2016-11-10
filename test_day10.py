import unittest


def process(data):
    numbers = list(map(int, str(data)))
    current_number = None
    count = 0
    output = []
    for number in numbers:
        if current_number is None:
            current_number = number
        if number != current_number:
            output.append(count)
            output.append(current_number)
            count = 0
        count += 1
        current_number = number

    output.append(count)
    output.append(current_number)

    return int("".join([str(i) for i in output]))


def iterate_processing(input_data, times):
    for i in range(times):
        input_data = process(input_data)
    return input_data


class TestDay10(unittest.TestCase):
    def test_1GoesTo11(self):
        self.assertEqual(11, process(1))

    def test_11Becomes21(self):
        self.assertEqual(21, process(11))

    def test_21Becomes1211(self):
        self.assertEqual(1211, process(21))

    def test_1211Becomes111221(self):
        self.assertEqual(111221, process(1211))

    def test_111221Becomes312211(self):
        self.assertEqual(312211, process(111221))

    def test_canIterate(self):
        data = 1
        data = iterate_processing(data, 2)
        self.assertEqual(21, data)

    @unittest.skip("skip part one")
    def testPartOne(self):
        data = iterate_processing(1321131112, 40)
        length = len(list(map(int, str(data))))
        self.assertEqual(length, 492982)

    @unittest.skip("skip part two")
    def testPartTwo(self):
        data = iterate_processing(1321131112, 50)
        length = len(list(map(int, str(data))))
        self.assertEqual(length, 6989950)
