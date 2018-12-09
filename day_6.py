"""
(1, 1), (8, 3) -> (5, 1), (3, 4)

(a, b), (c, d)

(a - c) + (b - d)
4
2
a a a a a . c c c c
a A a a a . c c c c
a a a d d e c c c c
a a d d d e c c C c
. . d D d e e c c c
b b . d e E e e c c
b B b . e e e e . .
b b b . e e e f f f
b b b . e e f f f f
b b b . f f f f F f
"""
import numpy as np
from scipy.spatial.distance import cityblock


from read_file import read_input


def get_area():
    """
    """
    coords_raw = read_input('input_6.txt')[:-1]
    coords = [(int(coord.split(', ')[0]), int(coord.split(', ')[1])) for coord in coords_raw]
    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]

    return max_x, max_y


def distances():
    """
    construct area
    for every point in the area, calculate distance between every input point and that point
    which ever point has the smallest manhattan distance, set that coordinates value to the
    integer value starting from 1
    if equidistant, equal 0
    """
    coords_raw = read_input('input_6.txt')[:-1]
    coords = [(int(coord.split(', ')[0]), int(coord.split(', ')[1])) for coord in coords_raw]
    max_x, max_y = get_area()
    grid = np.zeros((max_y+1, max_x+1))
    all_poss_coords = ((x, y) for x in range(max_x) for y in range(max_y))
    for coord in all_poss_coords:
        least = float('inf')
        least_point = None
        for i, point in enumerate(coords, 1):
            dist = cityblock(coord, point)
            if dist < least:
                least = dist
                least_point = i
        grid[coord[1], coord[0]] = least_point
    border_left = np.unique(grid[:, 0])
    border_right = np.unique(grid[:, -1])
    border_top = np.unique(grid[0])
    border_bottom = np.unique(grid[-1])
    border_nums = np.unique(np.concatenate([border_left, border_bottom, border_right, border_top]))
    grid[np.isin(grid, border_nums)] = 0

    return np.max(np.unique(grid, return_counts=True)[1])


if __name__ == '__main__':
    print(distances())
