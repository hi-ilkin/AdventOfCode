import numpy as np
from utils import timeit


@timeit
def solve_part_1(data):
    """
    For part 1, optimal position is simply median value

    :param data: List of positions
    :return: amount of required fuel
    """
    median = np.median(data)
    required_fuel = np.sum(np.abs(data - median))
    return required_fuel


def weighted_fuel_consumption(data, target_pos):
    n = np.abs(data - target_pos)
    return np.sum(n * (n + 1) / 2)


def solve_part_2(data):
    """
    For part 2, optimal position is somewhere around mean
    Checking -1 and +1 of mean will give us the answer

    :param data: List of positions
    :return: amount of required fuel
    """
    mean = int(np.round(np.mean(data)))

    fuel_consumptions = []
    for i in range(mean - 1, mean + 2):
        res = weighted_fuel_consumption(data, i)
        fuel_consumptions.append(res)
        print(f'{i}: {res}')

    return min(fuel_consumptions)


if __name__ == '__main__':
    fname = 'input.txt'
    inpt = np.array(list(map(int, open(fname).read().split(','))))
    required_fuel_amount = solve_part_2(inpt)
    print(f"{np.mean(inpt)} {np.median(inpt)}")
    print(f"Amount of fuel required is {required_fuel_amount}")
