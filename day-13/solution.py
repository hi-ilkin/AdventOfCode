from collections import defaultdict

import numpy as np

from utils import timeit


@timeit
def get_data(fname):
    is_fold = False
    folds = []

    indexes = defaultdict(list)

    for line in open(fname).readlines():
        if line.isspace():
            is_fold = True
            continue
        if is_fold:
            folds.append(line.strip().split(' ')[-1].split('='))
        else:
            y, x = list(map(int, line.strip().split(',')))
            indexes['x'].append(x)
            indexes['y'].append(y)

    # TODO: Change this part. Size of the board should be first fold of each axis * 2 + 1
    x_size = int(folds[1][1]) * 2 + 1
    y_size = int(folds[0][1]) * 2 + 1

    paper = np.zeros((x_size, y_size), dtype=np.int16)
    paper[indexes['x'], indexes['y']] = 1

    return paper, folds


def fold_once(paper, axis, index):
    if axis == 'y':
        part_1 = paper[:index, :]
        part_2 = np.flip(paper[index + 1:, :], 0)

    else:
        part_1 = paper[:, :index]
        part_2 = np.flip(paper[:, index + 1:], 1)

    return part_1 + part_2


@timeit
def fold_multiple(paper, folds):
    for fold in folds:
        axis, index = fold[0], int(fold[1])
        paper = fold_once(paper, axis, index)

    return paper


@timeit
def main():
    input_name = 'input.txt'
    p, f = get_data(input_name)

    folded = fold_multiple(p, f)
    h, w = folded.shape

    for r in range(h):
        for c in range(w):
            print(' 0' if folded[r, c] > 0 else ' .', end='')
        print()

    # print(folded)
    print(f'Dots: {np.count_nonzero(folded)}')


if __name__ == '__main__':
    main()
