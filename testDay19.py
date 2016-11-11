import unittest
import itertools


class operator(object):
    def __init__(self, character, substitution):
        self.character = character
        self.substitution = substitution

    def compare(self, other):
        if other == self.character:
            return True
        else:
            return False


def replace(string, operators):
    foundSubstitutions = []
    for idx, char in enumerate(string):
        for operator in operators:
            charLen = len(operator.character)
            if operator.compare(string[idx:idx+charLen]):
                newString = string[:idx] + operator.substitution + string[idx+charLen:]
                foundSubstitutions.append(newString)
    return foundSubstitutions


def get_unique_molecules(result):
    return [x for x, _ in itertools.groupby(sorted(result))]


def molecule_iterator(operators, stop):
    data = ["e"]
    iterations = 0
    newdata = []
    keepGoing = True
    while (keepGoing):
        iterations += 1
        for datum in data:
            newdata.extend(replace(datum, operators))
        if stop in newdata:
            keepGoing = False
        data = get_unique_molecules(newdata)
        newdata = [datum for datum in newdata if len(datum)<=len(stop)]  # strip out everything longer than the input, as the converters only ever make the sequence longer
        print(len(newdata), len(data), iterations)
        newdata = []

        if iterations>=250:
            break
    return iterations


class Test19(unittest.TestCase):

    def setUp(self):
        self.operators = []
        lines = open("testData/input19")
        lines = [line.rstrip("\n") for line in lines.readlines()]
        for line in lines[:-2]:
            first, second = line.split(" => ")
            self.operators.append(operator(first, second))
        self.calibration = lines[-1]

    def testReplacementH_HOOperator(self):
        self.assertEqual(replace("H", [operator("H", "HO")])[0], "HO")

    def testReplacementH_OHOperator(self):
        self.assertEqual(replace("H", [operator("H", "OH")])[0], "OH")

    def testReplacementO_HHOperator(self):
        self.assertEqual(replace("O", [operator("O", "HH")])[0], "HH")

    def testReplacementOfHOHCanMakeHOOHusingHO(self):
        ho = operator("H", "HO")
        self.assertEqual(replace("HOH", [ho])[0], "HOOH")

    def testReplacementOfHOHCanMakeHOHO(self):
        ho = operator("H", "HO")
        self.assertEqual(replace("HOH", [ho])[1], "HOHO")

    def testReplacementOfHOHCanMakeOHOH(self):
        ho = operator("H", "OH")
        self.assertEqual(replace("HOH", [ho])[0], "OHOH")

    def testReplacementOfHOHCanMakeHOOHUsingOH(self):
        ho = operator("H", "OH")
        self.assertEqual(replace("HOH", [ho])[1], "HOOH")

    def testReplacementCanMakeAllFiveMolecules(self):
        ho = operator("H", "HO")
        oh = operator("H", "OH")
        hh = operator("O", "HH")
        result = replace("HOH", [ho, oh, hh])
        self.assertEqual(len(result), 5)

    def testResultCanRecogniseDuplicateMolecules(self):
        ho = operator("H", "HO")
        oh = operator("H", "OH")
        hh = operator("O", "HH")
        result = replace("HOH", [ho, oh, hh])

        self.assertEqual(len(get_unique_molecules(result)), 4)

    def test_checkHOHOHOGives7UniqueMolecules(self):
        ho = operator("H", "HO")
        oh = operator("H", "OH")
        hh = operator("O", "HH")
        result = replace("HOHOHO", [ho, oh, hh])

        self.assertEqual(len(get_unique_molecules(result)), 7)

    def test_checkCaCanBeReplaced(self):
        CaF = operator("Ca", "F")
        self.assertEqual(replace("CaC", [CaF])[0], "FC")

    def testPartOne(self):
        result = replace(self.calibration, self.operators)
        unique = get_unique_molecules(result)
        self.assertEqual(len(unique), 535)

    def testeCanMakeOInOneStep(self):
        self.assertEqual(replace("e", [operator("e", "O")])[0], "O")

    def testeCanMakeHHInTwoSteps(self):
        operators = [operator("e", "O"), operator("O", "HH")]
        iterations = molecule_iterator(operators, "HH")

        self.assertEqual(2, iterations)

    def testeCanMakeHOHInTthreeSteps(self):
        operators = [operator("e", "O"), operator("O", "HH"), operator("H", "OH")]
        iterations = molecule_iterator(operators, "HOH")
        self.assertEqual(3, iterations)

    def testeCanMakeHOHOHOInSixSteps(self):
        operators = [operator("e", "H"),
                     operator("e", "O"),
                     operator("O", "HH"),
                     operator("H", "OH"),
                     operator("H", "HO")]
        iterations = molecule_iterator(operators, "HOHOHO")
        self.assertEqual(6, iterations)

    def testPartTwo(self):
        #answer is between 175 and 250
        iterations = molecule_iterator(self.operators, self.calibration)
        self.assertEqual(6, iterations)
