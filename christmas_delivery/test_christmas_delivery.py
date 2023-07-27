from christmas_delivery.christmas_delivery import *

obj = SantasSleight()


def test_sleight_two_elfs_two_toys():
    toy_machine = ["Present 1", "Present 2"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 1}
    loaded_sleight = obj.sleigh(toy_machine, elf_list, presents_by_family)
    assert len(loaded_sleight) == len(toy_machine)
    assert loaded_sleight == toy_machine


def test_sleight_two_elfs_one_toy():
    toy_machine = ["Present 1"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1}
    loaded_sleight = obj.sleigh(toy_machine, elf_list, presents_by_family)
    assert len(loaded_sleight) == len(toy_machine)
    assert loaded_sleight == toy_machine


def test_sleight_two_elfs_three_toys():
    toy_machine = ["Present 1", "Present 2", "Present 3"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 2}  # note two toys
    loaded_sleight = obj.sleigh(toy_machine, elf_list, presents_by_family)
    assert len(loaded_sleight) == len(toy_machine)
    assert loaded_sleight == toy_machine
