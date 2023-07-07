from christmas_delivery.christmas_delivery import *

obj = SantasSleight()

def test_sleight():
    toys_list = ["Toy Machine", "Toy Machine"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    assert obj.sleigh(toys_list, elf_list) == toys_list
