from anagram.anagram import *

obj = Anagram()


def test_read_input_data():
    print(obj.read_input_data(INPUT_FILE))


def test_anagram_game_one_match():
    original = "documenting"
    list_of_anagrams_to_check = ["object", "menu"]
    one_match = obj.anagram_game(original, list_of_anagrams_to_check)
    assert one_match[0] == "menu"


def test_anagram_game_two_matches():
    original = "documenting"
    list_of_anagrams_to_check = ["object", "menu", "mount"]
    one_match = obj.anagram_game(original, list_of_anagrams_to_check)
    assert len(one_match) == 2
    assert one_match[0] == "menu"
    assert one_match[1] == "mount"


def test_find_anagram():
    original = "documenting"
    anagram = "menu"
    assert obj.find_anagram(original, anagram)
