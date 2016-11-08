import unittest
import collections
import itertools


def permutationsOfHappiness(relationships, people):
    happy_maximum = 0
    for permutation in itertools.permutations(range(1, len(people))):
        permutation = list(permutation)
        permutation.insert(0, 0)  # locking down the first position speeds it up a lot
        happy_maximum = max(calculate_happiness(permutation, relationships), happy_maximum)
    return happy_maximum


def parseString(string):
    name, _, positive, number, _, _, _, _, _, _, other = string.rstrip(".").split(" ")
    number = int(number)
    if positive == "lose":
        number *= -1
    return name, other, number


def populateTable(indices):
    table = []
    for idx, _ in enumerate(indices):
        table.append((indices[idx - 1], indices[(idx + 1) % len(indices)]))
    return table


def get_table_happiness(table):
    happy_sum = 0
    for person in table:
        happy_sum += person[0] + person[1]
    return happy_sum


def add_to_relationships(relationships, people, parsed_string):
    name, other, number = parsed_string
    if name not in people:
        people.append(name)
    first = people.index(name)
    if other not in people:
        people.append(other)
    second = people.index(other)
    relationships[first][second] = number


def calculate_happiness(indices, relationships):
    table = populateTable(indices)
    happy_table = []
    for idx, relation in enumerate(table):
        a = relationships[indices[idx]][relation[0]]
        b = relationships[indices[idx]][relation[1]]
        happy_table.append((a, b))
    return get_table_happiness(happy_table)


class TestDay13(unittest.TestCase):

    def setUp(self):
        self.data = ["Alice would lose 2 happiness units by sitting next to Bob.",
                     "Alice would lose 62 happiness units by sitting next to Carol.",
                     "Alice would gain 65 happiness units by sitting next to David.",
                     "Alice would gain 21 happiness units by sitting next to Eric.",
                     "Alice would lose 81 happiness units by sitting next to Frank.",
                     "Alice would lose 4 happiness units by sitting next to George.",
                     "Alice would lose 80 happiness units by sitting next to Mallory.",
                     "Bob would gain 93 happiness units by sitting next to Alice.",
                     "Bob would gain 19 happiness units by sitting next to Carol.",
                     "Bob would gain 5 happiness units by sitting next to David.",
                     "Bob would gain 49 happiness units by sitting next to Eric.",
                     "Bob would gain 68 happiness units by sitting next to Frank.",
                     "Bob would gain 23 happiness units by sitting next to George.",
                     "Bob would gain 29 happiness units by sitting next to Mallory.",
                     "Carol would lose 54 happiness units by sitting next to Alice.",
                     "Carol would lose 70 happiness units by sitting next to Bob.",
                     "Carol would lose 37 happiness units by sitting next to David.",
                     "Carol would lose 46 happiness units by sitting next to Eric.",
                     "Carol would gain 33 happiness units by sitting next to Frank.",
                     "Carol would lose 35 happiness units by sitting next to George.",
                     "Carol would gain 10 happiness units by sitting next to Mallory.",
                     "David would gain 43 happiness units by sitting next to Alice.",
                     "David would lose 96 happiness units by sitting next to Bob.",
                     "David would lose 53 happiness units by sitting next to Carol.",
                     "David would lose 30 happiness units by sitting next to Eric.",
                     "David would lose 12 happiness units by sitting next to Frank.",
                     "David would gain 75 happiness units by sitting next to George.",
                     "David would lose 20 happiness units by sitting next to Mallory.",
                     "Eric would gain 8 happiness units by sitting next to Alice.",
                     "Eric would lose 89 happiness units by sitting next to Bob.",
                     "Eric would lose 69 happiness units by sitting next to Carol.",
                     "Eric would lose 34 happiness units by sitting next to David.",
                     "Eric would gain 95 happiness units by sitting next to Frank.",
                     "Eric would gain 34 happiness units by sitting next to George.",
                     "Eric would lose 99 happiness units by sitting next to Mallory.",
                     "Frank would lose 97 happiness units by sitting next to Alice.",
                     "Frank would gain 6 happiness units by sitting next to Bob.",
                     "Frank would lose 9 happiness units by sitting next to Carol.",
                     "Frank would gain 56 happiness units by sitting next to David.",
                     "Frank would lose 17 happiness units by sitting next to Eric.",
                     "Frank would gain 18 happiness units by sitting next to George.",
                     "Frank would lose 56 happiness units by sitting next to Mallory.",
                     "George would gain 45 happiness units by sitting next to Alice.",
                     "George would gain 76 happiness units by sitting next to Bob.",
                     "George would gain 63 happiness units by sitting next to Carol.",
                     "George would gain 54 happiness units by sitting next to David.",
                     "George would gain 54 happiness units by sitting next to Eric.",
                     "George would gain 30 happiness units by sitting next to Frank.",
                     "George would gain 7 happiness units by sitting next to Mallory.",
                     "Mallory would gain 31 happiness units by sitting next to Alice.",
                     "Mallory would lose 32 happiness units by sitting next to Bob.",
                     "Mallory would gain 95 happiness units by sitting next to Carol.",
                     "Mallory would gain 91 happiness units by sitting next to David.",
                     "Mallory would lose 66 happiness units by sitting next to Eric.",
                     "Mallory would lose 75 happiness units by sitting next to Frank.",
                     "Mallory would lose 99 happiness units by sitting next to George."]
        self.people = []
        self.relationships = collections.defaultdict(dict)

    def test_onePersonOnATableDoesntHateItself(self):
        table = [(0, 0)]
        self.assertEqual(0, get_table_happiness(table))

    def test_twoPeopleOnATableDontHateEachOther(self):
        table = [(0, 0), (0, 0)]
        self.assertEqual(0, get_table_happiness(table))

    def test_twoPeopleOnATableDoHateEachOther(self):
        table = [(-1, -1), (-2, -2)]
        self.assertEqual(-6, get_table_happiness(table))

    def test_threePeopleOnATableWorks(self):
        table = [(-1, 1), (-1, 1), (-1, 2)]
        self.assertEqual(1, get_table_happiness(table))

    def test_canGetCorrectScoreFromExampleTable(self):
        table = [(41, 46), (-2, 54), (-7, 83), (55, 60)]
        self.assertEqual(330, get_table_happiness(table))

    def test_givenASetOfIndicesIsTheTableCorrect(self):
        table = populateTable([0, 1, 2, 3])
        self.assertEqual(table[0], (3, 1))

    def test_givenALongerSetOfIndicesIsTheTableCorrect(self):
        table = populateTable([0, 1, 2, 3, 6, 5, 4])
        self.assertEqual(table[6], (5, 0))

    def test_populateHappinessFromDict(self):
        relationships = {
            0: {
                1: 1,
                2: 3,
                3: 4
            },
            1: {
                0: 0,
                2: 4,
                3: 6
            },
            2: {
                0: 0,
                1: 3,
                3: 4,
            },
            3: {
                0: -10,
                1: -3,
                2: -5
            }
        }

        self.assertEqual(calculate_happiness([0, 2, 1, 3], relationships), 7)

    def test_canParsePositiveText(self):
        string = "Alice would gain 54 happiness units by sitting next to Bob."
        name, other, number = parseString(string)
        self.assertEqual(name, "Alice")
        self.assertEqual(other, "Bob")
        self.assertEqual(number, 54)

    def test_canParseNegativeText(self):
        string = "Alice would lose 79 happiness units by sitting next to Carol."
        name, other, number = parseString(string)
        self.assertEqual(name, "Alice")
        self.assertEqual(other, "Carol")
        self.assertEqual(number, -79)

    def test_constructRelationships(self):
        string = "Alice would gain 54 happiness units by sitting next to Bob."
        add_to_relationships(self.relationships, self.people, parseString(string))
        self.assertEqual(self.relationships[0][1], 54)

        string = "Alice would lose 79 happiness units by sitting next to Carol."
        add_to_relationships(self.relationships, self.people, parseString(string))
        self.assertEqual(self.relationships[0][2], -79)

    def test_runExample(self):
        strings = ["Alice would gain 54 happiness units by sitting next to Bob.",
                   "Alice would lose 79 happiness units by sitting next to Carol.",
                   "Alice would lose 2 happiness units by sitting next to David.",
                   "Bob would gain 83 happiness units by sitting next to Alice.",
                   "Bob would lose 7 happiness units by sitting next to Carol.",
                   "Bob would lose 63 happiness units by sitting next to David.",
                   "Carol would lose 62 happiness units by sitting next to Alice.",
                   "Carol would gain 60 happiness units by sitting next to Bob.",
                   "Carol would gain 55 happiness units by sitting next to David.",
                   "David would gain 46 happiness units by sitting next to Alice.",
                   "David would lose 7 happiness units by sitting next to Bob.",
                   "David would gain 41 happiness units by sitting next to Carol."]

        for string in strings:
            add_to_relationships(self.relationships, self.people, parseString(string))
        expected = {0: {1: 54, 2: -79, 3: -2},
                    1: {0: 83, 2: -7, 3: -63},
                    2: {0: -62, 1: 60, 3: 55},
                    3: {0: 46, 1: -7, 2: 41}}
        self.assertEqual(expected, self.relationships)

        self.assertEqual(permutationsOfHappiness(self.relationships, self.people), 330)

    def test_partOne(self):
        for string in self.data:
            add_to_relationships(self.relationships, self.people, parseString(string))
        self.assertEqual(permutationsOfHappiness(self.relationships, self.people), 664)

    def test_partTwo(self):
        for string in self.data:
            add_to_relationships(self.relationships, self.people, parseString(string))
        for person in self.people[:]:
            add_to_relationships(self.relationships, self.people, (person, "Me", 0))
            add_to_relationships(self.relationships, self.people, ("Me", person, 0))
        self.assertEqual(permutationsOfHappiness(self.relationships, self.people), 640)
