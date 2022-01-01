import os
from collections import defaultdict

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


def depth_first(graph, current_vertex, visited, visited_list):
    if current_vertex == 'end':
        visited.append('end')
        visited_list.append(visited)
        return

    visited.append(current_vertex)

    for vertex in graph[current_vertex]:
        if vertex.isupper() or vertex not in visited:
            depth_first(graph, vertex, visited.copy(), visited_list)


@timeit
def main():
    fname = 'inputs/12.txt'
    visited_list = []
    graph = get_cave_map(fname)
    depth_first(graph, 'start', [], visited_list)



    print(f"Number of possible paths: {len(visited_list)}")


if __name__ == '__main__':
    main()
