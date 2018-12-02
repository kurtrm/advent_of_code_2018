"""
"""
from itertools import cycle


def read_input(filename):
    """
    """
    with open(f'inputs/{filename}') as f:
        file = f.read().split()

    return file


def calc_freq():
    """
    """
    return sum(eval(num) for num in read_input('input_1.txt'))


def double_freq():
    """
    """
    freqs = {}
    total = 0
    raw_freq_changes = read_input('input_1.txt')
    for freq in cycle(raw_freq_changes):
        total += eval(freq)
        try:
            freqs[total] += 1
            return total
        except KeyError:
            freqs[total] = 1


if __name__ == '__main__':
    print(double_freq())
