import numpy as np


def number_mask(*numbers):
    mask = np.uint16(0)
    for n in numbers:
        mask |= 1 << n
    return mask


def place_number(board, row, col, value):
    """PS: The unary bit is for determining whether a value has been set"""
    value = np.uint16(value)
    mask = number_mask(value)
    remove_mask = UNTOUCHED ^ mask

    # remove from possibilities in row
    board[row] &= remove_mask

    # remove from possibilities in col
    board[:, col] &= remove_mask

    # remove from possibilities in square
    square_row, square_col = 3 * (row // 3), 3 * (col // 3)
    board[square_row : square_row + 3, square_col : square_col + 3] &= remove_mask

    # set value in place
    board[row][col] = mask

    return board


def is_unresolved(value):
    return value & 1


def is_unambiguous(value):
    n = value >> 1
    return n.bit_count() == 1


UNTOUCHED = number_mask(*range(0, 11))

with open("0096_sudoku.txt") as f:
    games = f.read().strip().split("Grid ")[1:]

for game in games:
    # read in board from game string
    board = np.full((9, 9), UNTOUCHED, dtype=np.uint16)
    for r, row in enumerate(game.split("\n")[1:]):
        for c, value in enumerate(row):
            if value != "0":
                board = place_number(board, r, c, value)
    print(board)

    while np.any(is_unresolved(board)):
        unresolved_map = is_unresolved(board)
        unambiguous_map = is_unambiguous(board)
        easy_map = unresolved_map & unambiguous_map

        for (row, col), value in np.ndenumerate(board):
            if easy_map[row, col]:
                place_number(board, row, col, value - np.uint16(1))
                print(board)
        print(board)
        print(np.bitwise_count(board))
        print()
