from test_driven_development.fizz_buzz import fizz_buzz
import pytest


@pytest.mark.parametrize("input_int", [3, 6])
def test_print_fizz_when_n_is_3(input_int):
    output = fizz_buzz(input_int)
    assert output == "Fizz"
