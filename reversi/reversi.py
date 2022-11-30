# print 8x8 board filled with .

def print_board(cell):
    print("\n              Game Started")
    for i in range(8):
        if cell_logic("B") == "B":
            cell = "B"
        populate_row(cell)


def populate_cell(cell):
    for i in range(8):
        print(cell, end='     ')
    print("\n")


def populate_row(cell_value):
    populate_cell(cell_value)


def cell_logic(cell_value):
    if cell_value == "B":
        cell = "B"
    return cell
