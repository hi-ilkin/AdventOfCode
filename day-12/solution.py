from collections import defaultdict, deque

from utils import timeit


@timeit
def get_cave_map(fname):
    cave_map = defaultdict(list)
    for line in open(fname).readlines():
        d1, d2 = line.strip().split('-')
        cave_map[d1].append(d2)
        cave_map[d2].append(d1)

    return cave_map


def get_possible_neighbors(cur_node, cave_map, cur_route, route_stack):
    for node in cave_map[cur_node]:
        if node.islower() and node in cur_route and node == 'start':
            continue
        elif node == 'end':
            cur_route.append('end')
            return cur_route
        else:
            route_stack.append(node)

    next_node = route_stack.pop()
    cur_route.append(next_node)
    return get_possible_neighbors(next_node, cave_map, cur_route, route_stack)


def find_all_routes(cave_map):
    route_stack = deque()
    cur_route = ['start']

    res = get_possible_neighbors('start', cave_map, cur_route, route_stack)
    print(res)


if __name__ == '__main__':
    fname = 'small-input.txt'
    cm = get_cave_map(fname)
    print(cm)
    find_all_routes(cm)
