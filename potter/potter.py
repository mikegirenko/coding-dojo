BOOKS = ["first book", "second book", "third book", "fourth book", "fifth book"]
BASKET_ZERO = []  # basket is empty
BASKET_ONE = [BOOKS[0]]  # one book
BASKET_TWO = [BOOKS[0], BOOKS[0]]  # two identical books
BASKET_THREE = [BOOKS[0], BOOKS[1]]  # two different books - 5% discount


def calculate_price(basket):
    basket_cost = 0
    single_book_price = 8
    if len(basket) == 0:  # basket is empty
        basket_cost = 0
    if len(basket) == 1:  # one book
        basket_cost = single_book_price * 1
    if len(basket) == 2:
        if len(set(basket)) == 1:
            basket_cost = single_book_price * 2
        if len(set(basket)) == 2:  # 5% discount
            discount = ((single_book_price * 2) * 5) / 100
            basket_cost = (single_book_price * 2) - discount

    return basket_cost
