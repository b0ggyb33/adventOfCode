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
