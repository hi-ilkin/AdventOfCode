from utils import timeit


def get_data(fname):
    _, _, x, y = open(fname).readline().strip().split(' ')
    x, max_x = x.split('..')
    max_x = max_x.strip(',')
    min_x = x.split('=')[-1]

    y, max_y = y.split('..')
    min_y = y.split('=')[-1]
    return list(map(int, (min_x, max_x, min_y, max_y)))


def part_1(yf_min):
    vy = (abs(yf_min) - 1)
    h_max = ((vy + 0.5) ** 2) / 2
    return round(h_max)


def did_hit(vx, vy, min_x, max_x, min_y, max_y):
    x = 0
    y = 0

    while True:
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True

        if x > max_x:
            return False

        if vx == 0 and not min_x <= x <= max_x:
            return False
        if vx == 0 and y < min_y:
            return False

        if vx > 0:
            vx -= 1
        else:
            vx = 0

        vy -= 1
        x += vx
        y += vy


def part_2(min_x, max_x, min_y, max_y):
    counter = 0
    y_min = max(abs(min_y), abs(max_y))
    for y in range(-y_min, y_min + 10):
        for x in range(max_x + 10):
            if did_hit(x, y, min_x, max_x, min_y, max_y):
                counter += 1
    return counter


@timeit
def main():
    min_x, max_x, min_y, max_y = get_data('inputs/17.txt')
    res_1 = part_1(min_y)
    res_2 = part_2(min_x, max_x, min_y, max_y)
    print(f'17a: {res_1}')
    print(f'17b: {res_2}')
