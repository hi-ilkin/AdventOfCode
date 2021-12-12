import numpy as np

from utils import timeit


def get_data(fname, width=10, height=10):
    lines = open(fname).readlines()
    data = np.zeros((width, height), dtype=np.int16)

    for row in range(height):
        for col in range(width):
            data[row, col] = int(lines[row][col])

    return data


def is_valid(x, y, w, h):
    return 0 <= x < w and 0 <= y < h


def update_adjacent(data, rows, cols, width, height, flash_list):
    directions = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]

    for x, y in zip(rows, cols):
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if is_valid(nx, ny, width, height) and data[nx, ny] != 0 and flash_list[nx, ny] == 0:
                data[nx, ny] += 1

    return data


@timeit
def solve_problem(data, steps=2, width=10, height=10):
    total_flash_count = 0

    for step in range(steps):
        data += 1

        data = np.where(data > 9, 0, data)
        is_flashed = np.count_nonzero(data == 0) > 0
        tmp_flash_list = np.where(data == 0, 1, 0)

        while is_flashed:
            rows, cols = np.where(tmp_flash_list == 1)
            data = update_adjacent(data, rows, cols, width, height, tmp_flash_list)

            tmp_flash_list = np.where(tmp_flash_list == 1, 2, tmp_flash_list)
            data = np.where(data > 9, 0, data)
            tmp_flash_list = np.where((data == 0) & (tmp_flash_list == 0), 1, tmp_flash_list)

            is_flashed = np.count_nonzero(tmp_flash_list == 1) > 0

        cur_flash_count = np.count_nonzero(data == 0)
        total_flash_count += cur_flash_count
        if cur_flash_count == width * height:
            print(f'Octopuses flashed simultaneously at step : {step + 1}')

    print(f'Total flash count is {total_flash_count}')
    return data


if __name__ == '__main__':
    input_name = 'input.txt'
    inpt_data = get_data(input_name)

    output = solve_problem(inpt_data, steps=300)

    # Control data is from example output. Using this to validate result
    # control_data = get_data('control.txt')
    # print(f'Control data and output is same: {np.array_equal(control_data, output)}')
