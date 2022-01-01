import os
from collections import defaultdict, Counter

from utils import timeit


@timeit
def get_cave_map(fname):
    cave_map = defaultdict(list)
    print(os.getcwd())
    for line in open(fname).readlines():
        d1, d2 = line.strip().split('-')
        cave_map[d1].append(d2)
        cave_map[d2].append(d1)

    return cave_map


def should_visit_next(vertex, visited, part):
    c1 = vertex.isupper() or vertex not in visited
    if c1:
        return c1

    if part == 2:
        if vertex in ['start', 'end']:
            return False
        counter = Counter(list(filter(lambda x: x.islower() and x not in ['start', 'end'], visited))).values()
        c2 = max(counter if len(counter) > 0 else [0]) <= 1
        return c2


def depth_first(graph, current_vertex, visited, visited_list, part=1):
    if current_vertex == 'end':
        visited.append('end')
        visited_list.append(visited)
        return

    visited.append(current_vertex)

    for vertex in graph[current_vertex]:
        if should_visit_next(vertex, visited, part):
            depth_first(graph, vertex, visited.copy(), visited_list, part)


def solve_part_1(graph):
    visited_list = []
    depth_first(graph, 'start', [], visited_list, part=1)
    return len(visited_list)


def solve_part_2(graph):
    visited_list = []
    depth_first(graph, 'start', [], visited_list, part=2)
    return len(visited_list)


@timeit
def main():
    fname = 'inputs/12.txt'
    graph = get_cave_map(fname)
    res_1 = solve_part_1(graph)
    res_2 = solve_part_2(graph)
    print(f'1a: {res_1}')
    print(f'1b: {res_2}')


if __name__ == '__main__':
    main()
