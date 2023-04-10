from cupcake.cupcake import *
obj = Cupcake()


def test_cupcake():
    assert obj.name()[0] == "Cake"
