"""
program to load Santa's Sleigh
Currently only one Elf can put a present on his Sleigh at a time
Santa wants to be able to be able to use multiple Elves
"""

toy_machine = ["Present 1", "Present 2", "Present 3"]
elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
presents_by_family = {"Smith family": 1, "Kaie family": 2}


class SantasSleight:
    def sleigh(self, toys_list: list, elf_list: list, presents_by_family: dict) -> list:
        loaded_sleight = []
        family_with_many_presents = False
        for k, v in presents_by_family.items():
            if v > 1:
                family_with_many_presents = True
        i = 0  # it keeps removing first elf
        elf_went_on_delivery = []
        while len(toys_list) != len(loaded_sleight):
            for toy in toys_list:
                if len(toys_list) <= len(elf_list):
                    loaded_sleight.append(toy)
                if len(toys_list) > len(elf_list):  # to handle more toys than elfs
                    elf_went_on_delivery.append(elf_list[i])
                    if not family_with_many_presents:
                        elf_list.pop(i)
                    if family_with_many_presents:
                        elf_list = elf_list
                    loaded_sleight.append(toy)
                    if len(elf_list) == 0:
                        elf_list.append(elf_went_on_delivery[-1])
                        loaded_sleight.append(toy)

        return loaded_sleight


if __name__ == "__main__":
    obj = SantasSleight()
    sleight = obj.sleigh(toy_machine, elf_list, presents_by_family)
    print("Santa's Sleigh has", sleight)
