def get_floor(string_input, return_basement_index=False):
    floor = 0
    basement_index = None
    for idx, item in enumerate(string_input):
        if item == ")":
            floor -= 1
        else:
            floor += 1

        if basement_index is None and return_basement_index and floor < 0:
            basement_index = idx+1  # needs to be 1-indexed not zero

    if not return_basement_index:
        return floor
    else:
        return floor, basement_index


def get_wrapping_volume(string_input):
    l, w, h = [int(item) for item in string_input.split("x")]
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l), l*w*h+min(2*l+2*w, 2*l+2*h, 2*w+2*h)


def wrap_all_presents():
    wrapping_sum = ribbon_sum = 0
    for line in open("presentFile"):
        wrapping, ribbon = get_wrapping_volume(line.strip("\n"))
        wrapping_sum += wrapping
        ribbon_sum += ribbon
    return wrapping_sum, ribbon_sum

from collections import defaultdict

class Deliverer(object):
    def __init__(self):
        self.houses = defaultdict(int)
        self.last_house = (0, 0)
        self.houses[self.last_house] = 1

    def visit_house(self, char):
        if char == "^":
            new_house = (self.last_house[0], self.last_house[1]+1)
        elif char == "v":
            new_house = (self.last_house[0], self.last_house[1]-1)
        elif char == "<":
            new_house = (self.last_house[0]-1, self.last_house[1])
        else:
            new_house = (self.last_house[0]+1, self.last_house[1])
        self.last_house = new_house
        self.houses[new_house] += 1


def get_houses_visited(string):

    santa = Deliverer()
    robosanta = Deliverer()

    for idx, item in enumerate(string):
        if idx % 2 == 0:
            courier = robosanta
        else:
            courier = santa

        courier.visit_house(item)

    return len(set(santa.houses.keys()+robosanta.houses.keys()))

from hashlib import md5

class Md5Solver(object):

    def string_starts_with_n_zeros(self, string, number_of_leading_zeros):
        return string.startswith('0'*number_of_leading_zeros)

    def get_md5(self, string):
        return md5(string).hexdigest()

    def concatenate_hash(self, base, extension):
        return base+str(extension)

    def solve(self, hash_base, number_of_zeros):
        minimum_hash_extension = 0
        test_hash = "111111"  # dummy value to initialise test_hash that will not pass the while test
        while not self.string_starts_with_n_zeros(self.get_md5(test_hash), number_of_zeros):
            minimum_hash_extension += 1
            test_hash = self.concatenate_hash(hash_base, minimum_hash_extension)
        return str(minimum_hash_extension)


class NiceStringFinder(object):

    def contains_three_vowels(self,string):
        vowels='aeiou'
        return sum([letter in vowels for letter in string])>=3

    def contains_double_letter(self,string):
        for idx,character in enumerate(string):
            if character in string[idx+1:idx+2]:
                return True
        return False

    def contains_naughty_substring(self,string):
        naughty_substrings=["ab","cd","pq","xy"]
        return any([naughty_string in string for naughty_string in naughty_substrings])

    def containsADoublePair(self,string):
        for idx,char in enumerate(string):
            if string[idx:idx+2] in string[idx+2:]:
                return True
        return False

    def contains_sandwich(self,string):
        for idx,char in enumerate(string):
            if char in string[idx+2:idx+3]:
                return True
        return False

    def isNice(self,string):
        return self.contains_three_vowels(string) and self.contains_double_letter(string) and not self.contains_naughty_substring(string)

    def isNicePart2(self,string):
        return self.containsADoublePair(string) and self.contains_sandwich(string)
