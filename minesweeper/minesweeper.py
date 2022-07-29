import random


def minesweeper(n):
    grid = [[0 for row in range(n)] for column in range(n)]

    for num in range(2):
        x = random.randint(0,4)
        y = random.randint(0,4)
        grid[y][x] = 'X'

    for row in grid:
        print(" ".join(str(cell) for cell in row))
        print("")

