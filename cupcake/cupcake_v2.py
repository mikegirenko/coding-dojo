# a Class which returns base
# a Class which inherits base and applies toppings (in a method)
# make it a bundle (order is "cupcake and cookie, with toppings")
# bundle of bundles (order is "cupcake and cookie, with toppings" AND "2 cookies, with toppings")
# bundle and single cake (order is "cupcake and cookie, without toppings" AND "cupcake with toppings")
# so, order dictates bundle and total price

# 07/06/23 giving up on this kata

class Base:
    cake = ["Cupcake", "Cookie"]


class Toppings(Base):
    # this_cupcake = Base.cupcake
    toppings = ["Black Chocolate", "Peanuts", "Sprinkles"]


class Order(Toppings):
    def user_input(self) -> list:
        user_input = input("What is your order: ")

        return user_input

    def order_price(self, order):
        price = 0
        order_list = []
        order_list.append(order)
        for item in order_list:
            if item == "Cupcake":
                price = "$1"

        return price


if __name__ == "__main__":
    obj = Order()
    ordered_by_user = obj.user_input()
    print("You ordered", obj.order_price(ordered_by_user))  # Cupcake
