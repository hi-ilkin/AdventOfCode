"""
Solution explaniation
Order of the characters are not preserved, so direct mapping is not possible. Eg, `be` and `eb` both represents 1.
4 Numbers (1,7,4,8) is known by their lenght. From 1 and 4 we can find two key character sets
1 gives us right top and bottom leds and
4 gives us leds of 1 + left top and middle ones.
By using those information, we can find remaining numbers
3 - len 5 and right and no left
0 - len 6 and right and no left
9 - len 6 and right and left
2 - len 5 and no right and no left
5 - len 6 and no right and left
6 - len 6 and no right and left
"""
from utils import timeit


def get_data(fn):
    lines = open(fn).readlines()
    data = []
    for line in lines:
        inp, out = line.split(' | ')
        data.append((inp.strip().split(' '), out.strip().split(' ')))

    return data


def solve_part_1(data):
    res = 0
    for inp, out in data:
        filtered = list(filter(lambda x: len(x) in (2, 4, 3, 7), out.strip('\n').split(' ')))
        print(f'{out.strip()} -> {filtered}')
        res += len(filtered)
    return res


def does_contain(a, b):
    return len(set(b) - set(a)) == 0


def get_number(segment, right_side, left_middle):
    nums_by_size = {2: 1, 4: 4, 3: 7, 7: 8}
    cur_number = nums_by_size.get(len(segment), None)

    if cur_number is None:
        if does_contain(segment, right_side):
            if len(segment) == 5:
                cur_number = 3
            else:
                if does_contain(segment, left_middle):
                    cur_number = 9
                else:
                    cur_number = 0
        else:
            if len(segment) == 6:
                cur_number = 6
            else:
                if does_contain(segment, left_middle):
                    cur_number = 5
                else:
                    cur_number = 2

    return cur_number


def get_special_characters(inp):
    specials = []
    numbers_by_length = {2: 1, 3: 7, 4: 4, 7: 8}

    for segment in inp:
        segment = sorted(segment)
        number = numbers_by_length.get(len(segment), None)
        if number is not None:
            specials.append((segment, number))

    return specials


def solve_part_2_better(data):
    output_nums = []

    for inp, out in data:
        numbers = {}
        tmp_output_nums = []

        specials = get_special_characters(inp)
        right, left = None, None

        for k, v in specials:
            numbers[''.join(k)] = v
            if v == 1:
                right = k
            elif v == 4:
                left = k

        left = set(left) - set(right)

        for segment in inp:
            segment_splitted = sorted(segment)
            merged_segment = ''.join(segment_splitted)
            if merged_segment not in numbers:
                cur_number = get_number(segment_splitted, right, left)
                numbers[merged_segment] = cur_number

        for segment in out:
            segment_splitted = sorted(segment)
            merged_segment = ''.join(segment_splitted)
            if merged_segment not in numbers:
                cur_number = get_number(segment_splitted, right, left)
                numbers[merged_segment] = cur_number
                tmp_output_nums.append(cur_number)
            else:
                tmp_output_nums.append(numbers[merged_segment])

        output_nums.append(int(''.join(map(str, tmp_output_nums))))

    return output_nums


if __name__ == '__main__':
    fname = 'input.txt'
    inpt_data = get_data(fname)
    output_numbers = solve_part_2_better(inpt_data)

    print(f'Result: {sum(output_numbers)}')
