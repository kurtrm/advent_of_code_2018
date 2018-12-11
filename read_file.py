"""
"""


def read_input(filename, separator='\n'):
    """
    """
    with open(f'inputs/{filename}') as f:
        file = f.read().split(separator)

    return file
