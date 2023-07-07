"""
program to load Santa's Sleigh
Currently only one Elf can put a present on his Sleigh at a time

Alabaster Snowball, Bushy Evergreen, Pepper Minstix, Shinny Upatree,
Sugarplum Mary, and Wunorse Openslae
"""

elf_list = ["Alabaster Snowball", "Bushy Evergreen"]
toys_list = ["Toy Machine", "Toy Machine", "Toy Machine"]

class SantasSleight:
    def sleigh(self, toys_list:list, elf_list:list) -> list:
        loaded_sleight = []
        i = 0  # keep removing first elf
        for toy in toys_list:
            if not len(elf_list) == 0:  # need to handle 3 toys and 2 elfs
                elf_list.pop(i)
                loaded_sleight.append(toy)

        return loaded_sleight


if __name__ == "__main__":
    obj = SantasSleight()
    sleight = obj.sleigh(toys_list, elf_list)
    print("Santa's Sleigh has", sleight)
