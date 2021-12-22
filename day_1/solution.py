from utils import timeit


@timeit
def solve_part_1(data):
    return len([data[i] for i in range(len(data) - 1, 1, -1) if data[i] > data[i - 1]])


@timeit
def solve_part_2(data):
    prev_sum = None
    counter = 0

    for i in range(3, len(data) + 1):
        cur_sum = sum(data[i - 3:i])

        if prev_sum is not None and cur_sum > prev_sum:
            counter += 1
        prev_sum = cur_sum

    return counter


@timeit
def get_data():
    data = list(map(int, open('inputs/1.txt', 'r')))
    return data


def main():
    data = get_data()
    res_1 = solve_part_1(data)
    res_2 = solve_part_2(data)
    print(f'1a: {res_1}')
    print(f'1b: {res_2}')
