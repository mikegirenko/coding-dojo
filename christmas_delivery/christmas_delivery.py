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
        elf_went_on_delivery = []
        for toy in toys_list:
            if len(toys_list) <= len(elf_list):
                # elf_went_on_delivery.append(elf_list[i])
                #elf_list.pop(i)
                loaded_sleight.append(toy)
            if len(toys_list) > len(elf_list):   # to handle 3 toys and 2 elfs
                elf_went_on_delivery.append(elf_list[i])
                elf_list.pop(i)
                loaded_sleight.append(toy)
                if len(elf_list) == 0:
                    elf_list.append(elf_went_on_delivery[-1])
                    loaded_sleight.append(toy)

        return loaded_sleight
# TODO next User Story 3

if __name__ == "__main__":
    obj = SantasSleight()
    sleight = obj.sleigh(toys_list, elf_list)
    print("Santa's Sleigh has", sleight)
