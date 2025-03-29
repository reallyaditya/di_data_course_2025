# import enchant
from itertools import permutations


class AnagramChecker:
    """
    A class to check if a word is a valid English word and to find its anagrams.
    """

    def __init__(self, word):
        """
        Initializes the AnagramChecker with a word.

        :param word: The word to check for anagrams.
        :raises ValueError: If the word is not a valid English word.
        """
        with open("/Users/aditya/Projects/dev_institute_2025/week4/sowpods.txt") as f:
            self.english_words = [
                cleaned_word.strip() for cleaned_word in f.readlines()
            ]

        if self.is_valid_word(word):
            self.word = word
        else:
            raise ValueError("The word is not in the english dictionary")

    def is_valid_word(self, word: str) -> bool:
        """
        Checks if a word is a valid English word.

        :param word: The word to check.
        :return: True if the word is a valid English word, False otherwise.
        """
        if word.upper() in self.english_words:
            return True
        return False

    def __get_anagrams(self):
        """
        Generates all possible anagrams of the word.

        :return: A list of all possible anagrams of the word.
        """
        return list(permutations(self.word))

    def valid_anagram_list(self):
        """
        Filters the anagrams to return only the valid English words.

        :return: A list of valid English word anagrams.
        """
        return [
            "".join(word)
            for word in self.__get_anagrams()
            if self.is_valid_word("".join(word))
        ]
