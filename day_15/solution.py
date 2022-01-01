import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from utils import timeit


def get_data(fname):
    cave_map = []
    for line in open(fname).readlines():
        cave_map.append(list(map(int, list(line.strip()))))

    return np.array(cave_map)


def solve(cave_map):
    grid = Grid(matrix=cave_map)
    start = grid.node(0, 0)
    h, w = cave_map.shape
    end = grid.node(w - 1, h - 1)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    cost = 0
    for p in path[1:]:
        cost += cave_map[p[::-1]]

    # print(path)
    # print(runs)
    # print(grid.grid_str(path=path, start=start, end=end))

    return cost


def extend_map(cave_map, duplicate, axis):
    new_map = cave_map.copy()

    for d in range(duplicate):
        new_slice = (cave_map + 1) % 10
        new_slice = np.where(new_slice == 0, 1, new_slice)
        new_map = np.append(new_map, new_slice, axis)
        cave_map = new_slice.copy()

    return new_map


def get_larger_map(cave_map, duplicate=4):
    cave_map = extend_map(cave_map, duplicate, 1)
    cave_map = extend_map(cave_map, duplicate, 0)

    return cave_map


@timeit
def main():
    cave_map = get_data('inputs/15.txt')
    res_1 = solve(cave_map)
    print(f"15a: {res_1}")

    large_map = get_larger_map(cave_map)
    res_2 = solve(large_map)
    print(f"15b: {res_2}")
