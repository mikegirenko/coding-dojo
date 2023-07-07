from christmas_delivery.christmas_delivery import *


def test_sleight():
    present = "Toy Machine"
    elf = "Alabaster Snowball"
    assert sleigh(present, elf) == [present]
