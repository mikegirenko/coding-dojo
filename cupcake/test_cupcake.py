from unittest.mock import patch

from cupcake.cupcake import *

obj = Cupcake()


def test_name():
    assert obj.name() in [
        "Cupcake",
        "Cookie",
        "Cupcake with Chocolate",
        "Cookie with Chocolate",
        "Cookie with Peanuts",
    ]


def test_price():
    item = "Cupcake"
    assert obj.price(item) == 1
    item = "Cookie"
    assert obj.price(item) == 2
    item = "Cupcake with Chocolate"
    assert obj.price(item) == 1.1
    item = "Cookie with Chocolate"
    assert obj.price(item) == 2.1
    item = "Cookie with Peanuts"
    assert obj.price(item) == 2.2


# Bundle with 1 Cupcake
def test_bundle_price_one_item():
    items_in_bundle = ["Cupcake"]
    assert obj.bundle_price(items_in_bundle) == 1


# Bundle with 1 Cupcake and 1 Cookie
def test_bundle_price_two_items():
    items_in_bundle = ["Cupcake", "Cookie"]
    assert obj.bundle_price(items_in_bundle) == 2.7


# Bundle with 2 Cupcake and 1 Cookie
def test_bundle_price_three_items():
    items_in_bundle = ["Cupcake", "Cupcake", "Cookie"]
    assert obj.bundle_price(items_in_bundle) == 3.6
