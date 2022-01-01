"""
Generic filter applies given function to each element.
It passes item itself and all of its adjacent cells as a 1D array.
so. left-top is 0, target cell is 4 and bottom right is 9th element of array.
"wrap" param helps rotation.

"""
import numpy as np
from scipy.ndimage import generic_filter


def get_data(fname):
    d = {".": 0, ">": 1, "v": 2}
    sea_map = []
    for line in open(fname).readlines():
        sea_map.append([d[x] for x in list(line.strip())])
    return np.array(sea_map, dtype=np.uint8)


def move_east(a):
    if a[4] == 0 and a[3] == 1:
        return 1
    if a[4] == 1 and a[5] == 0:
        return 0
    return a[4]


def move_south(a):
    if a[4] == 0 and a[1] == 2:
        return 2
    if a[4] == 2 and a[7] == 0:
        return 0
    return a[4]


def main():
    arr = get_data('inputs/25.txt')

    i = 1
    while True:
        prev = arr
        arr = generic_filter(arr, move_east, size=3, mode="wrap")
        arr = generic_filter(arr, move_south, size=3, mode="wrap")
        if np.array_equal(prev, arr):
            print(i)
            break
        i += 1
