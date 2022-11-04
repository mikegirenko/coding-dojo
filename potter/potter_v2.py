from collections import Counter

BASKET = [{"count": 2, "title": "first book"}, {"count": 2, "title": "second book"},
          {"count": 2, "title": "third book"}, {"count": 1, "title": "fourth book"},
          {"count": 1, "title": "fifth book"}]
BOOK_PRICE = 8
DISCOUNTS = {2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}


def calculate_price(basket):
    basket_cost = 0
    books_list_flat = []
    set_sizes = []
    sets = []
    for books_set in BASKET:
        for i in range(0, books_set["count"]):
            books_list_flat.append(books_set["title"])
    while books_list_flat:
        unique_books = set(books_list_flat)
        set_sizes.append(len(unique_books))
        sets.append(unique_books)
        for b in unique_books:
            books_list_flat.remove(b)
    set_sizes = Counter(set_sizes)
    while set_sizes[3] and set_sizes[5]:
        set_sizes[3] -= 1
        set_sizes[5] -= 1
        set_sizes[4] += 2
    best_list = list(set_sizes.elements())
    basket_cost = sum(set_price(a) for a in best_list)

    return basket_cost


def set_price(set_size):
    return BOOK_PRICE * set_size * DISCOUNTS.get(set_size, 1)
