from christmas_delivery.christmas_delivery import *

obj = SantasSleight()

def test_sleight_two_elfs_two_toys():
    toy_machine = ["Present 1", "Present 2"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 1}
    assert len(obj.sleigh(toy_machine, elf_list, presents_by_family)) == len(toy_machine)


def test_sleight_two_elfs_one_toy():
    toy_machine = ["Present 1"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 1}
    assert len(obj.sleigh(toy_machine, elf_list, presents_by_family)) == len(toy_machine)


def test_sleight_two_elfs_three_toys():
    toy_machine = ["Present 1", "Present 2", "Present 3"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 1, "Kaie family": 1}
    assert len(obj.sleigh(toy_machine, elf_list, presents_by_family)) == len(toy_machine)


def test_delivery_by_family():
    toy_machine = ["Present 1", "Present 2", "Present 3"]
    elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
    presents_by_family = {"Smith family": 2, "Kaie family": 1}
    assert len(obj.sleigh(toy_machine, elf_list, presents_by_family)) == len(toy_machine)

# one elf delivers all presents per family
# if Smith family has 2 presents, "Alabaster Snowball" will take then and deliver
