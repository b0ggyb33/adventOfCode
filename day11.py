import unittest
import string


def iterate(string_under_test):
    string_under_test = list(string_under_test)
    for index in range(len(string_under_test)-1, -1, -1):
        if string_under_test[index] == "z":
            string_under_test[index] = "a"
            if index == 0:
                string_under_test.insert(0, "a")
        else:
            new_character = chr(ord(string_under_test[index]) + 1)
            string_under_test[index] = new_character
            break

    return "".join(string_under_test)


doubles = [character + character for character in string.ascii_lowercase]


def is_valid(string_under_test):
    for item in ["i", 'o', 'l']:
        if item in string_under_test:
            return False

    count = 0
    for char in doubles:
        if char in string_under_test:
            count += 1
            if count > 1:
                break

    if count < 2:
        return False

    for index in range(len(string_under_test)-2):
        if (ord(string_under_test[index+1]) - ord(string_under_test[index]) == 1) and \
                (ord(string_under_test[index+2]) - ord(string_under_test[index+1]) == 1):
            return True
    return False


def get_next_valid_string(string_under_test):
    new_string = string_under_test
    while not is_valid(new_string) or (new_string == string_under_test):
        new_string = iterate(new_string)
    return new_string


class TestDay11(unittest.TestCase):
    def testaiteratestob(self):
        self.assertEqual(iterate("a"), "b")

    def testbiteratestoc(self):
        self.assertEqual(iterate("b"), "c")

    def testziteratestoaa(self):
        self.assertEqual(iterate("z"), "aa")

    def testaaiteratestoab(self):
        self.assertEqual(iterate("aa"),"ab")

    def testaziteratestoba(self):
        self.assertEqual(iterate("az"), "ba")

    def testaaziteratestoaba(self):
        self.assertEqual(iterate("aaz"), "aba")

    def testabdisvalid(self):
        self.assertFalse(is_valid("abd"))

    def testabcisnotvalid(self):
        self.assertTrue(is_valid("abcffgg"))

    def testbcdisnotvalid(self):
        self.assertTrue(is_valid("rrbcdee"))

    def testiisnotValid(self):
        self.assertFalse(is_valid("i"))

    def testoisnotValid(self):
        self.assertFalse(is_valid("o"))

    def testlisnotvalid(self):
        self.assertFalse(is_valid("l"))

    def testContainsTwoPairs(self):
        self.assertTrue(is_valid("aafbbcde"))

    def testDoesNotContainTwoPairs(self):
        self.assertFalse(is_valid("fbbcde"))

    def testIsValidExamples(self):
        self.assertFalse(is_valid("hijklmmn"))
        self.assertFalse(is_valid("abbceffg"))
        self.assertFalse(is_valid("abbcegjk"))

        self.assertEqual(get_next_valid_string("abcdefgh"), "abcdffaa")

    def testPartOne(self):
        self.assertEqual(get_next_valid_string("cqjxjnds"), "cqjxxyzz")

    def testPartTwo(self):
        self.assertEqual(get_next_valid_string("cqjxxyzz"), "cqkaabcc")
