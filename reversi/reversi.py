BOARD = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "B", "W", ".", ".", "."],
    [".", ".", ".", "W", "B", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
]


def print_board(board):
    print("\n            Game starts")
    for row in board:
        print(row)


def populate_board(board):
    return board


def check_if_can_be_flipped_row(row, my_disk):
    index_to_flip = 0
    for disk in row:
        if disk != my_disk and disk != ".":
            index_to_flip = row.index(disk)

    return index_to_flip


def check_if_can_be_flipped_column(rows, my_disk):
    index_to_flip = 0
    index_to_check = 0
    row_to_check = 0
    my_disk_index = 0
    my_disk_row_index = 0
    row_counter = 0
    # find my_disk index in a row which contains it
    for row in rows:
        if my_disk in row:
            my_disk_index = row.index(my_disk)
            my_disk_row_index = row_counter
        row_counter += 1
    print("my_disk_index", my_disk_index)
    print("my_disk_row_index", my_disk_row_index)
    # while index_to_check < 8: # need to check an index, for each row
    #     if
    #         # B is [1][3]. so check [0][3]?
    #         row_to_check += 1
    #     index_to_check += 1

    return index_to_flip
