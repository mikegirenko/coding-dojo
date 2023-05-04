import random


class Cupcake:
    def name(self) -> list:
        item_name = ["Cake", "Cookie", "Cake with Chocolate", "Cookie with Chocolate", "Cookie Peanuts",
                     "Cookie with Peanuts and Chocolate"]
        item_index = random.randint(0, 5)

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


    def bundle_price_v2(self, bundle):
        total_price = 0
        counter = 0
        #while counter < len(bundle):



        return total_price


    def bundle_price(self, item_count, price):
        total_price = 0
        if item_count == 1:
            total_price = price
        if item_count > 1:
            price_temp = price * item_count
            discount = (price_temp / 100) * 10
            total_price = price_temp - discount

        return total_price


if __name__ == "__main__":
    obj = Cupcake()
    item = obj.name()
    price = obj.price(item)
    print("The cake is", item, ". The price is $", price)

    items = []
    for i in range(0, 2):
        items.append(obj.name())
    print("The bundle is", items)
    # ['Cake with Chocolate', 'Cookie Peanuts']

    for item in items:
        pass
