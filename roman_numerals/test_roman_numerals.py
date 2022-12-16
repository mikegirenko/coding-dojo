from roman_numerals.roman_numerals import Roman

obj = Roman()


def test_number_below_eleven():
    assert obj.number_below_eleven(0) == "Romans did not have zero"
    assert obj.number_below_eleven(1) == "I"
    assert obj.number_below_eleven(3) == "III"
    assert obj.number_below_eleven(4) == "IV"
    assert obj.number_below_eleven(5) == "V"
    assert obj.number_below_eleven(8) == "VIII"
    assert obj.number_below_eleven(9) == "IX"
    assert obj.number_below_eleven(10) == "X"


def test_number_below_fifty():
    assert obj.number_below_fifty(11) == "XI"
