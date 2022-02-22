from test_driven_development.fizz_buzz import fizz_buzz


def test_print_fizz():
    output = fizz_buzz(3)
    assert output == "Fizz"
