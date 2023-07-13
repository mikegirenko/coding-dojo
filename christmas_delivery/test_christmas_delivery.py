from christmas_delivery.christmas_delivery import *

obj = SantasSleight()

def test_sleight_two_elfs_two_toys():
    toys_list = ["Toy Machine", "Toy Machine"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    assert obj.sleigh(toys_list, elf_list) == toys_list


def test_sleight_two_elfs_one_toy():
    toys_list = ["Toy Machine"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    assert obj.sleigh(toys_list, elf_list) == toys_list


def test_sleight_two_elfs_three_toys():
    toys_list = ["Toy Machine", "Toy Machine", "Toy Machine"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    assert obj.sleigh(toys_list, elf_list) == toys_list
