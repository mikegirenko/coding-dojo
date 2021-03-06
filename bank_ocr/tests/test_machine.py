"""
List of tests:

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


def test_machine_extracts_account_numbers():
    letter = ["m", 1, 2, 3, "W", 4]
    expected_letter = ["?", 1, 2, 3, "?", 4]
    obj = Machine(letter)
    assert expected_letter == obj.extract_account_numbers()


def test_populate_number_one():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_one()


def test_populate_number_two():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_two()


def test_populate_number_three():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_three()


def test_populate_number_four():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_four()


def test_populate_number_five():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_five()


def test_populate_number_six():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_six()


def test_populate_number_seven():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_seven()


def test_populate_number_eight():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_eight()


def test_populate_number_nine():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_number_nine()


def test_populate_file_with_real_account_numbers():
    letter = [1, 2, 3, "W", 4, 5, 6, 7, 8, 9]
    obj = Machine(letter)
    obj.populate_file_with_real_account_numbers()


def test_check_if_account_number_has_valid_checksum_validates_account_numbers():
    letter = [11, 0, 0, 0, 0, 0, 0, 0, 0]
    obj = Machine(letter)
    assert obj.check_if_account_number_has_valid_checksum()


def test_check_if_account_number_has_another_valid_checksum_validates_account_numbers():
    letter = [0, 0, 0, 0, 0, 0, 0, 5, 1]
    obj = Machine(letter)
    assert obj.check_if_account_number_has_valid_checksum()


def test_check_if_account_number_has_valid_checksum_does_not_validate_account_numbers():
    letter = [-2, 0, 0, 0, 0, 0, 0, 0, 1]
    obj = Machine(letter)
    assert not obj.check_if_account_number_has_valid_checksum()


def test_all_zeroes():
    letter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    obj = Machine(letter)
    obj.accept_letter_and_produce_file()


def test_all_ones():
    letter = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    obj = Machine(letter)
    obj.accept_letter_and_produce_file()


def test_random_numbers():
    letter = [0, 0, 0, 0, 0, 0, 0, 5, 1]
    obj = Machine(letter)
    obj.accept_letter_and_produce_file()


def test_illegible_characters():
    letter = [4, "?", 0, 0, 0, 0, 0, 5, 1]
    obj = Machine(letter)
    obj.accept_letter_and_produce_file()
