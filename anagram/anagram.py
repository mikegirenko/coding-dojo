from typing import List

INPUT_FILE = "word_list.txt"
"""
Write a program that generates all two-word anagrams of the string “documenting”.
You must focus on the readability of your code, and you must not include any kind of
documentations to it. F. e., documenting = menu
"""


class Anagram:
    def read_input_data(self, a_file) -> List[str]:
        with open(a_file, "r") as file:
            read_data = file.read()
        list_of_strings = read_data.split("\n")
        list_of_data = []
        for string in list_of_strings:
            temp = string.split()
            for word in temp:
                list_of_data.append(word)

        return list_of_data

    def anagram_game(self, original, list_of_anagrams_to_check) -> List:
        anagram = []
        for word in list_of_anagrams_to_check:
            if self.find_anagram(original, word):
                anagram.append(word)

        return anagram

    def find_anagram(
        self, original, anagram
    ):  # documenting is original, menu is anagram
        letter_count = 0
        anagram_flag = False
        for letter in anagram:
            if letter in original:
                letter_count += 1
        if letter_count == len(anagram):
            anagram_flag = True

        return anagram_flag


if __name__ == "__main__":
    obj = Anagram()
    original_word = "documenting"
    words_list = obj.read_input_data(INPUT_FILE)
    print(
        "Anagrams of the string 'documenting' are",
        obj.anagram_game(original_word, words_list),
    )
    original_word = "bread"
    words_list = obj.read_input_data(INPUT_FILE)
    print(
        "Anagrams of the string 'bread' are",
        obj.anagram_game(original_word, words_list),
    )