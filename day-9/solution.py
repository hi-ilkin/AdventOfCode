import numpy as np
from utils import timeit


def get_board(filename):
    data = list(map(str.strip, open(filename).readlines()))
    height = len(data)
    width = len(data[0])
    board = np.zeros((height, width), dtype=np.int16)

    for r in range(height):
        for c in range(width):
            board[r][c] = int(data[r][c])

    return board


def is_dir_invalid(r, c, w, h):
    return r < 0 or c < 0 or r >= h or c >= w


def is_lowest_points(board, r, c, w, h):
    directons = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y in directons:
        nr = x + r
        nc = y + c
        if is_dir_invalid(nr, nc, w, h):
            continue

        if board[r, c] >= board[nr, nc]:
            return False

    return True


@timeit
def solve_part_1(board):
    height, width = board.shape
    lowest_points = []

    for r in range(height):
        for c in range(width):
            if is_lowest_points(board, r, c, width, height):
                lowest_points.append(board[r, c])

    return sum(lowest_points) + len(lowest_points)


def create_basin(r, c, board, w, h, basin, visited):
    directons = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if board[r, c] == 9:
        return None, visited

    if visited[r, c] == 1:
        return None, visited

    visited[r, c] = 1

    for x, y in directons:
        nr = x + r
        nc = y + c
        if is_dir_invalid(nr, nc, w, h):
            continue
        create_basin(nr, nc, board, w, h, basin, visited)

    basin.append(board[r, c])
    return basin, visited


@timeit
def solve_part_2(board):
    height, width = board.shape
    visited = np.zeros(board.shape, dtype=np.int16)
    basins = []
    basin_sizes = []

    for r in range(height):
        for c in range(width):
            basin = []
            basin, visited = create_basin(r, c, board, width, height, basin, visited)
            if basin is None:
                continue
            basins.append(basin)
            basin_sizes.append(len(basin))

    # print(basins)
    return np.prod(sorted(basin_sizes, reverse=True)[:3])


if __name__ == '__main__':
    fname = 'input.txt'
    input_board = get_board(fname)
    result = solve_part_2(input_board)
    print(result)
