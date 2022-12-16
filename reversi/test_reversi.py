from reversi.reversi import *


def test_print_board():
    print_board(BOARD)


def test_populate_board():
    board = populate_board(BOARD)
    assert board[3][3] == "B"


def test_check_if_can_be_flipped_row():
    row = [".", ".", ".", "B", "W", ".", ".", "."]
    index_can_be_flipped = check_if_can_be_flipped_row(row, "B")
    assert index_can_be_flipped == 4


def test_check_if_can_be_flipped_column():
    rows = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "W", "B", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]
    index_can_be_flipped = check_if_can_be_flipped_column(rows, "B")
    assert index_can_be_flipped == 0
