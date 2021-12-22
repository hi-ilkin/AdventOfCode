import argparse

import numpy as np


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default=1, help='part to solve')
    parser.add_argument('--input', help="path to input data", required=True)

    return parser.parse_args()


def get_start_end(p1, p2):
    return min(p1, p2), max(p1, p2)


def run(filepath, b_size=10, part=1, debug=False):
    board = np.zeros((b_size, b_size), dtype=np.uint8)
    fp = open(filepath)

    for line in fp.readlines():
        y1, x1, y2, x2 = list(map(int, line.replace(' -> ', ',').strip().split(',')))
        if x1 == x2:
            start_y, end_y = get_start_end(y1, y2)
            for y in range(start_y, end_y + 1):
                board[x1][y] += 1

        elif y1 == y2:
            start_x, end_x = get_start_end(x1, x2)
            for x in range(start_x, end_x + 1):
                board[x][y1] += 1

        else:
            if part != 2:
                continue

            if x2 > x1:
                if y2 > y1:
                    dx, dy = 1, 1
                else:
                    dx, dy = 1, -1
            else:
                if y2 > y1:
                    dx, dy = -1, 1
                else:
                    dx, dy = -1, -1

            dist_x = abs(x2 - x1)
            dist_y = abs(y2 - y1)
            assert f"Distances are not equal: dist_x: {dist_x} dist_y: {dist_y} ", dist_x == dist_y
            for i in range(dist_x + 1):
                board[x1 + i * dx][y1 + i * dy] += 1

        if debug:
            print(f"y1: {y1}, x1: {x1}, y2:{y2}, x2:{x2}")
            print(board)
    print(f"Number of overlapping lines: {np.sum(board >= 2)}")


if __name__ == '__main__':
    args = get_arguments()

    part = int(args.part)
    filename = args.input
    run(filename, b_size=1000, part=2)
