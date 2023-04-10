from cupcake.cupcake import *

obj = Cupcake()


def test_cupcake():
    assert obj.name() in ["Cake", "Cookie", "Cake with Chocolate", "Cookie with Chocolate", "Cookie Peanuts",
                          "Cookie with Chocolate and Peanuts", "Cookie with Peanuts and Chocolate"]


def test_price():
    item = "Cake"
    assert obj.price(item) == 1
