from bank_ocr.code.machine import Machine


def test_machine_accepts_letter_and_produces_file():
    letter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    machine_object = Machine(letter)
    machine_object.accept_letter_and_produce_file()
