from bank_ocr.code.machine import Machine


def test_machine_accepts_letter_and_produces_file():
    letter = ["This letter has account number", 1, 2, 3, "M", 4, 5, 6, 7, "Spam", 8, 9, "K"]
    machine_object = Machine(letter)
    machine_object.accept_letter_and_produce_file()
