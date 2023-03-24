from anagram.anagram import *

obj = Anagram()


def test_read_input_data():
    print(obj.read_input_data(INPUT_FILE))


def test_anagram_game():
    obj.anagram_game()


def test_find_anagram():
    original = "documenting"
    anagram = "menu"
    assert obj.find_anagram(original, anagram)
