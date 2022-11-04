from potter.potter_v2 import *


def test_calculate_basket_price():
    assert calculate_price(BASKET) == 51.2
