BOOKS = ["first book", "second book", "third book", "fourth book", "fifth book"]
BASKET_EMPTY = []  # basket is empty
BASKET_ONE_BOOK = [BOOKS[0]]  # one book
BASKET_TWO_BOOKS = [BOOKS[0], BOOKS[0]]  # two identical books
BASKET_TWO_DIFF_BOOKS = [BOOKS[0], BOOKS[1]]  # two different books - 5% discount
BASKET_THREE_BOOKS = [BOOKS[0], BOOKS[1], BOOKS[2]]  # three different books - 10% discount
BASKET_FOUR_BOOKS = [BOOKS[0], BOOKS[1], BOOKS[2], BOOKS[3]]  # four different books - 20% discount
BASKET_FIVE_BOOKS = [BOOKS[0], BOOKS[1], BOOKS[2], BOOKS[3], BOOKS[4]]  # five different books - 25% discount


def calculate_price(basket):
    basket_cost = 0
    single_book_price = 8
    if len(basket) == 0:  # basket is empty
        basket_cost = 0
    if len(basket) == 1:  # one book
        basket_cost = single_book_price * 1
    if len(basket) == 2:  # two books
        if len(set(basket)) == 1:
            basket_cost = single_book_price * 2
        if len(set(basket)) == 2:  # 5% discount
            discount = ((single_book_price * 2) * 5) / 100
            basket_cost = (single_book_price * 2) - discount
    if len(basket) == 3:  # three books
        if len(set(basket)) == 1:
            basket_cost = single_book_price * 3
        if len(set(basket)) == 2:  # 5% discount + one book cost
            discount = ((single_book_price * 2) * 5) / 100
            basket_cost = ((single_book_price * 2) - discount) + single_book_price
        if len(set(basket)) == 3:  # 10% discount
            discount = ((single_book_price * 3) * 10) / 100
            basket_cost = (single_book_price * 3) - discount
    if len(basket) == 4:  # four books
        if len(set(basket)) == 1:
            basket_cost = single_book_price * 4
        if len(set(basket)) == 2:  # 5% discount + 5% discount
            discount = ((single_book_price * 2) * 5) / 100
            basket_cost = ((single_book_price * 2) - discount) + ((single_book_price * 2) - discount)
        if len(set(basket)) == 3:  # 10% discount + one book cost
            discount = ((single_book_price * 3) * 10) / 100
            basket_cost = ((single_book_price * 3) - discount) + single_book_price
        if len(set(basket)) == 4:  # 20% discount
            discount = ((single_book_price * 4) * 20) / 100
            basket_cost = ((single_book_price * 4) - discount)
    if len(basket) == 5:  # five books
        if len(set(basket)) == 1:
            basket_cost = single_book_price * 5
        if len(set(basket)) == 2:  # 5% discount + 10% discount
            discount_one = ((single_book_price * 2) * 5) / 100
            discount_two = ((single_book_price * 3) * 10) / 100
            basket_cost = ((single_book_price * 2) - discount_one) + ((single_book_price * 3) - discount_two)
        if len(set(basket)) == 3:  # 10% discount + one book cost + one book cost
            discount = ((single_book_price * 3) * 10) / 100
            basket_cost = ((single_book_price * 3) - discount) + single_book_price + single_book_price
        if len(set(basket)) == 4:  # 5% discount + one book cost + one book cost + one book cost
            discount = ((single_book_price * 2) * 5) / 100
            basket_cost = ((single_book_price * 2) - discount) + single_book_price + single_book_price + single_book_price
        if len(set(basket)) == 5:  # 25% discount
            discount = ((single_book_price * 5) * 25) / 100
            basket_cost = ((single_book_price * 5) - discount)

    return basket_cost
