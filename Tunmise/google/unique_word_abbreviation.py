from typing import Collection


class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        self.abbr_to_counts = Collection.defaultdict(int)
        self.words_set = set(dictionary)
        for word in self.words_set:
            abbr = self.word_to_abbr(word)
            self.abbr_to_counts[abbr] += 1

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        abbr = self.word_to_abbr(word)
        if word in self.words_set:
            return self.abbr_to_counts[abbr] <= 1 
        else:
            return self.abbr_to_counts[abbr] < 1 

    def word_to_abbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]