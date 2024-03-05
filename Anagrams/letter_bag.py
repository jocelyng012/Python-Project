'''
CS 211 Winter 2024 Project 2
Author: Jocelyn Guan
Credit: Isabel Dalisay
Description: Anagram 
'''

"""A bag of letters for finding anagrams.
Associates a cardinality (count) with each character
in the bag.
"""

def normalize(phrase: str) -> list[str]:
    """Normalize word or phrase to the
    sequence of letters we will try to match, discarding
    anything else, such as blanks and apostrophes.
    Return as a list of individual letters.
    """
    new_list = []
    for i in phrase:
        if i.isalpha():
            i = i.lower()
            new_list.append(i)
    return new_list


class LetterBag:
    """A bag (also known as a multiset) is
    a map from keys to non-negative integers.
    A LetterBag is a bag of single character
    strings.
    """
    def __init__(self, word=""):
        """Create a LetterBag"""
        self.word = word.strip()
        normal = normalize(self.word)
        self.length = len(normal)
        self.letters = {}
        for i in normal:
            if i in self.letters:
                self.letters[i] += 1
            else:
                self.letters[i] = 1

    def __len__(self):
        return self.length

    def __str__(self):
        return self.word

    def __repr__(self):
        counts = [f"{ch}:{n}" for ch, n in self.letters.items() if n > 0]
        return f'LetterBag({self.word}/[{", ".join(counts)}])'

    def contains(self, other: "LetterBag") -> bool:
        """Determine whether enough of each letter in
        other LetterBag are contained in this LetterBag.
        """
        keys_list = sorted(other.letters.keys())
        keyslist_len = len(keys_list)
        for i in range(keyslist_len):
            if keys_list[i] not in sorted(self.letters.keys()):
                return False
        for i in range(len(keys_list)):
            if self.letters[keys_list[i]] < other.letters[keys_list[i]]:
                return False
        return True

    def copy(self) -> "LetterBag":
        """Make a copy before mutating."""
        copy_ = LetterBag()
        copy_.word = self.word
        copy_.letters = self.letters.copy() 
        copy_.length = self.length
        return copy_

    def take(self, other: "LetterBag") -> "LetterBag":
        """Return a LetterBag after removing
        the letters in other.  Raises exception
        if any letters are not present.
        """
        bag = self.copy()
        if not bag.contains(other):
            raise Exception 
        for key, value in other.letters.items():
            bag.letters[key] = bag.letters[key] - value
        bag.length = len(bag)-len(other)
        return bag


