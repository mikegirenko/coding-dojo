from bank_ocr.code.machine import Machine


# def test_machine_accepts_letter_which_has_account_number_with_valid_checksum_and_produces_file():
#     letter_has_account_number_with_valid_checksum = [11,  0,  0,  0,  0,  0,  0,  0,  0]
#     machine_object = Machine(letter_has_account_number_with_valid_checksum)
#     machine_object.accept_letter_and_produce_file()


def test_machine_accepts_letter_which_has_account_number_with_invalid_checksum_and_produces_file():
    letter_has_account_number_with_invalid_checksum = [-2,  0,  0,  0,  0,  0,  0,  0,  1]
    machine_object = Machine(letter_has_account_number_with_invalid_checksum)
    machine_object.accept_letter_and_produce_file()
