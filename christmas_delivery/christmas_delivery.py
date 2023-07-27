"""
program to load Santa's Sleigh
Currently only one Elf can put a present on his Sleigh at a time
Santa wants to be able to be able to use multiple Elves

Alabaster Snowball, Bushy Evergreen, Pepper Minstix, Shinny Upatree,
Sugarplum Mary, and Wunorse Openslae
"""

elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
toys_list = ["Toy Machine 1", "Toy Machine 2", "Toy Machine 3"]
presents_by_family = {"Smith family": 1, "Kaie family": 2}

class SantasSleight:
    def sleigh(self, toys_list:list, elf_list:list, presents_by_family:dict) -> list:
        loaded_sleight = []
        i = 0  # keep removing first elf
        elf_went_on_delivery = []
        for toy in toys_list:
            while len(toys_list) != len(loaded_sleight):
                if len(toys_list) <= len(elf_list):
                    loaded_sleight.append(toy)
                if len(toys_list) > len(elf_list):   # to handle more toys than elfs
                    elf_went_on_delivery.append(elf_list[i])
                    elf_list.pop(i)
                    loaded_sleight.append(toy)
                    if len(elf_list) == 0:
                        elf_list.append(elf_went_on_delivery[-1])
                        loaded_sleight.append(toy)

        return loaded_sleight
# TODO next User Story 3 - deliver presents by family when possible.

if __name__ == "__main__":
    obj = SantasSleight()
    sleight = obj.sleigh(toys_list, elf_list, presents_by_family)
    print("Santa's Sleigh has", sleight)
