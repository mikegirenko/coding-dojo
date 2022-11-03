from potter.potter import calculate_price, BASKET_ZERO, BASKET_ONE, BASKET_TWO, BASKET_THREE


def test_calculate_basket_zero_price():
    assert calculate_price(BASKET_ZERO) == 0


def test_calculate_basket_one_price():
    assert calculate_price(BASKET_ONE) == 8


def test_calculate_basket_two_price():
    assert calculate_price(BASKET_TWO) == 16


def test_calculate_basket_three_price():
    assert calculate_price(BASKET_THREE) == 15.2
