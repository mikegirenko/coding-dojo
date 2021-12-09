"""
List of tests:



Lets assume letter is a list populated with letters and numbers
Lets assume file is another list, correctly populated and printed to console
"""
from bank_ocr.code.machine import Machine


def test_machine_accepts_letter():
    letter = ["m", 2]
    obj = Machine(letter)
    letter_accepted = obj.letter
    assert letter_accepted


def test_machine_reads_letter():
    letter = [3, 7, "k"]
    obj = Machine(letter)
    assert letter == obj.letter


def test_machine_validates_and_populates_file():
    letter = ["m", 1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    assert letter != obj.validate_letter_and_populate_file()
