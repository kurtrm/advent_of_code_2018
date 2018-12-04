"""
"""
import numpy as np

from read_file import read_input


def parse_rectangles():
    """
    """
    file = read_input('input_3.txt')[:-1]
    for line in file:
        coords = line.split('@')[1].split(':')
        start, offset = coords[0].split(','), coords[1].split('x')
        left_s, left_e = int(start[0]), int(start[0]) + int(offset[0])
        top_s, top_e = int(start[1]), int(start[1]) + int(offset[1])
        yield left_s, left_e, top_s, top_e


def count_overlaps():
    """
    """
    fabric = np.zeros((1000, 1000))
    coords = parse_rectangles()
    for coord in coords:
        left_s, left_e, top_s, top_e = coord
        fabric[top_s:top_e, left_s: left_e] += 1
    return fabric


def find_single(matrix):
    """
    """
    coords = parse_rectangles()
    for fabric_id, coord in enumerate(coords, start=1):
        left_s, left_e, top_s, top_e = coord
        if (matrix[top_s:top_e, left_s: left_e] == 1).all():
            return fabric_id


if __name__ == '__main__':
    matrix = count_overlaps()
    print(find_single(matrix))
