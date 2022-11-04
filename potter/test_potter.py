from potter.potter import *


def test_calculate_basket_zero_price():
    assert calculate_price(BASKET_EMPTY) == 0


def test_calculate_basket_one_price():
    assert calculate_price(BASKET_ONE_BOOK) == 8


def test_calculate_basket_two_price():
    assert calculate_price(BASKET_TWO_BOOKS) == 16


def test_calculate_basket_three_price():
    assert calculate_price(BASKET_TWO_DIFF_BOOKS) == 15.2


def test_calculate_basket_four_price():
    assert calculate_price(BASKET_THREE_BOOKS) == 21.6


def test_calculate_basket_five_price():
    assert calculate_price(BASKET_FOUR_BOOKS) == 25.6


def test_calculate_basket_six_price():
    assert calculate_price(BASKET_FIVE_BOOKS) == 30.0

