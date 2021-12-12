import numpy as np


def is_open_character(c):
    return c in ['[', '(', '{', '<']


def solve_problem(fname):
    file = open(fname)

    penalty_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    penalty_score = 0

    autocomplete_score_map = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    autocomplete_scores = []

    for line in file.readlines():
        line = line.strip()
        stack = []
        invalid_line = False
        for c in line:
            if is_open_character(c):
                stack.append(c)

            else:
                item = stack.pop()
                if c == ']' and item != '[':
                    penalty_score += penalty_map[c]
                    invalid_line = True
                    break
                elif c == ')' and item != '(':
                    penalty_score += penalty_map[c]
                    invalid_line = True
                    break
                elif c == '}' and item != '{':
                    penalty_score += penalty_map[c]
                    invalid_line = True
                    break
                elif c == '>' and item != '<':
                    penalty_score += penalty_map[c]
                    invalid_line = True
                    break

        if not invalid_line:
            score = 0
            while len(stack) > 0:
                item = stack.pop()
                score = score * 5 + autocomplete_score_map[item]
            autocomplete_scores.append(score)

    return penalty_score, np.median(autocomplete_scores)


if __name__ == '__main__':
    input_file_name = 'input.txt'
    res_part_1, res_part_2 = solve_problem(input_file_name)
    print(f'Result for part 1: {res_part_1} and part 2: {res_part_2}')
