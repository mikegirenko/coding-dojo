from unittest.mock import patch

from cupcake.cupcake import *

obj = Cupcake()


def test_cupcake():
    assert obj.name() in ["Cake", "Cookie", "Cake with Chocolate", "Cookie with Chocolate", "Cookie Peanuts",
                          "Cookie with Chocolate and Peanuts", "Cookie with Peanuts and Chocolate"]


def test_price():
    item = "Cake"
    assert obj.price(item) == 1


@patch("cupcake.cupcake.Cupcake.name")
def test_bundle_price_one_item(mock_name):
    bundle = 1
    mock_name.return_value = "Cookie Peanuts"
    assert obj.bundle_price(bundle) == 2.2

#TODO next - Bundle with 1 Cupcake and 1 Cookie
def test_bundle_price_two_items():
    item_count = 2
    price = 2
    assert obj.bundle_price(item_count, price) == 3.6


def test_bundle_price_v2():
    names = []
    for i in range(0, 2):
        names.append(obj.name())
    print(names)
    prices = []
    for name in names:
        prices.append(obj.price(name))

    print(prices)
    i = 0
    whole_bundle = []
    while i < len(names):
        one_item = {"item": names[i], "price": prices[i]}
        whole_bundle.append(one_item)
        i += 1
    print(whole_bundle) # list of dictionaries
# [{'item': 'Cake with Chocolate', 'price': 1.1}]
# [{'item': 'Cookie with Chocolate', 'price': 2.1}, {'item': 'Cookie with Chocolate', 'price': 2.1}]
