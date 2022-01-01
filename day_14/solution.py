from collections import Counter, defaultdict

from utils import timeit


def parse_data(fn):
    rules = {}
    template, rules_raw = open(fn).read().split('\n\n')
    for r in rules_raw.split('\n'):
        rule, ins = r.split(' -> ')
        rules[rule] = ins

    return template, rules


def solve(template, rules, steps):
    pairs = defaultdict(int)
    for i in range(len(list(template)) - 1):
        pairs[template[i:i + 2]] += 1

    for _ in range(steps):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            new_element = rules[pair]
            new_pairs[pair[0] + new_element] += count
            new_pairs[new_element + pair[1]] += count

        pairs = new_pairs.copy()

    number_of_chars = defaultdict(int)
    for pair, count in pairs.items():
        number_of_chars[pair[0]] += count
    number_of_chars[template[-1]] += 1
    counts = Counter(number_of_chars).values()

    return max(counts) - min(counts)


@timeit
def main():
    template, rules = parse_data('inputs/14.txt')
    res_1 = solve(template, rules, 10)
    res_2 = solve(template, rules, 40)
    print(f'14a: {res_1}')
    print(f'14b: {res_2}')


if __name__ == '__main__':
    main()
