"""
List of tests
test_machine_accepts_letter
test_machine_reads_letter
test_machine_creates_file

Lets assume letter is a list populated with letters and numbers
Lets assume file is just a print to console
"""
from bank_ocr.code.machine import Machine


def test_machine_accepts_letter():
    letter = ["m", 2]
    obj = Machine(letter)
    letter_accepted = obj.letter
    assert letter_accepted
