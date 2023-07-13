from christmas_delivery.christmas_delivery import *

obj = SantasSleight()

def test_sleight_two_elfs_two_toys():
    toys_list = ["Toy Machine 1", "Toy Machine 2"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 1}
    assert len(obj.sleigh(toys_list, elf_list, presents_by_family)) == len(toys_list)


def test_sleight_two_elfs_one_toy():
    toys_list = ["Toy Machine 1"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 1}
    assert len(obj.sleigh(toys_list, elf_list, presents_by_family)) == len(toys_list)


def test_sleight_two_elfs_three_toys():
    toys_list = ["Toy Machine 1", "Toy Machine 2", "Toy Machine 3"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 1}
    assert len(obj.sleigh(toys_list, elf_list, presents_by_family)) == len(toys_list)
