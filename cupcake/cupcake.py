import random


class Cupcake:
    def name(self) -> list:
        item_name = ["Cake", "Cookie", "Cake with Chocolate", "Cookie with Chocolate", "Cookie Peanuts",
                     "Cookie with Chocolate and Peanuts", "Cookie with Peanuts and Chocolate"]
        item_index = random.randint(0, 6)

        return item_name[item_index]

    def price(self, item):
        price = 0
        if item == "Cake":
            price = 1
        if item == "Cookie":
            price = 2
        if item == "Cake with Chocolate":
            price = 1.1
        if item == "Cookie with Chocolate":
            price = 2.1
        if item == "Cookie Peanuts":
            price = 2.2

        return price



if __name__ == "__main__":
    obj = Cupcake()
    item = obj.name()
    price = obj.price(item)
    print("The cake is", item, " The price is", price)
