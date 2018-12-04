"""
"""


def read_input(filename):
    """
    """
    with open(f'inputs/{filename}') as f:
        file = f.read().split('\n')

    return file
