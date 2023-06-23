import random


class Cupcake:
    def name(self) -> list:
        item_name = [
            "Cupcake",
            "Cookie",
            "Cupcake with Chocolate",
            "Cookie with Chocolate",
            "Cookie with Peanuts",
        ]
        item_index = random.randint(0, 4)

        return item_name[item_index]

    def price(self, item) -> int:
        price = 0
        if item == "Cupcake":
            price = 1
        if item == "Cookie":
            price = 2
        if item == "Cupcake with Chocolate":
            price = 1.1
        if item == "Cookie with Chocolate":
            price = 2.1
        if item == "Cookie with Peanuts":
            price = 2.2

        return price

    def bundle_price(self, items_in_bundle) -> int:
        price_without_discount = []
        price_temp = 0
        total_price = 0
        for item in items_in_bundle:
            price_without_discount.append(self.price(item))
        if len(items_in_bundle) == 0:
            total_price = 0
        if len(items_in_bundle) == 1:
            total_price = price_without_discount[0]
        # The price of a bundle is 10% less than prices of each cake.
        if len(items_in_bundle) > 1:
            for price in price_without_discount:
                price_temp += price
            discount = (price_temp / 100) * 10
            total_price = price_temp - discount

        return total_price


if __name__ == "__main__":
    obj = Cupcake()
    item = obj.name()
    price = obj.price(item)
    print(f"The cake is {item}. The price is ${price}")

    items = []
    for i in range(0, 2):  # this makes bundle with 2 items
        items.append(obj.name())
    bundle_price = obj.bundle_price(items)
    print(f"The bundle is {items}." "The bundle price is", "%.2f" % bundle_price)

    items = []
    for i in range(0, 3):  # this makes bundle with 3 items
        items.append(obj.name())
    bundle_price = obj.bundle_price(items)
    print(f"The bundle is {items}." "The bundle price is", "%.2f" % bundle_price)
