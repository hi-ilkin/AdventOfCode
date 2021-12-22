import numpy as np
from utils import timeit


@timeit
def good_solution(filename):
    """Not by me , but it is very cool"""
    data = [open(filename).read().count(str(i)) for i in range(0, 9)]

    for day in range(256):
        data[(day + 7) % 9] += data[day % 9]
    print(sum(data))


@timeit
def bad_solution(ages):
    for i in range(80):
        ages -= 1
        new_lantern_count = np.sum(ages < 0)
        ages = np.concatenate((ages, np.array([8] * new_lantern_count, dtype=np.int8)))
        ages = np.where(ages < 0, 6, ages)
        # print(f"After {i:3} days: {ages}, {len(ages)}")
        print(f"{i} , {len(ages):_}")

    print(f"After {i} days number of lanterns: {len(ages):_}")


if __name__ == '__main__':
    fname = 'input.txt'
    fp = open(fname)
    lantern_ages = np.array(list(map(int, fp.readlines()[0].split(','))), np.int8)

    rand_sol(lantern_ages)
    good_solution(fname)
