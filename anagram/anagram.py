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
        list_of_data = read_data.split("\n")

        return list_of_data


    def anagram_game(self):
        pass

    def find_anagram(self, original, anagram):  # documenting is original, menu is anagram
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
    obj.anagram_game()
