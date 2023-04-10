from cupcake.cupcake import *

obj = Cupcake()


def test_cupcake():
    assert obj.name() in ["Cake", "Cookie", "Cake with Chocolate", "Cookie with Chocolate", "Cookie Peanuts",
                          "Cookie with Chocolate and Peanuts", "Cookie with Peanuts and Chocolate"]


def test_price():
    item = "Cake"
    assert obj.price(item) == 1


def test_bundle_price_one_item():
    item_count = 1
    price = 2
    assert obj.bundle_price(item_count, price) == 1


def test_bundle_price_two_items():
    item_count = 2
    price = 2
    assert obj.bundle_price(item_count, price) == 3.6
