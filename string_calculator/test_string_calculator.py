from string_calculator.string_calculator import StringCalculator

obj = StringCalculator()


def test_many_numbers():
    assert obj.add("1, 2, 3") == 6


def test_empty_string():
    assert obj.add("") == "0"


def test_new_line_character():
    assert obj.add("1\n2,3") == 6
