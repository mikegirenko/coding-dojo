from monty_hall.monty_hall import *


def test_choose_option():
    o = choose_option(OPTIONS)
    assert o in OPTIONS
