"""
"""
from string import ascii_lowercase


def read_input(filename):
    """
    """
    with open(f'inputs/{filename}') as f:
        file = f.read()

    return file


def change_polymer(file):
    """
    """
    i = 0
    while True:
        try:
            capital = file[i].isupper()
            if capital:
                if file[i].lower() == file[i+1]:
                    del file[i:i+2]
                    i -= 1
                else:
                    i += 1
            else:
                if file[i].upper() == file[i+1]:
                    del file[i:i+2]
                    i -= 1
                else:
                    i += 1
        except IndexError:
            break
    return len(file)


def remove_same_type():
    """
    """
    shortest_len = float('inf')
    file = list(read_input('input_5.txt'))[:-1]
    for letter in ascii_lowercase:
        copy_file = file.copy()
        try:
            while True:
                copy_file.remove(letter)
        except ValueError:
            pass
        try:
            while True:
                copy_file.remove(letter.upper())
        except ValueError:
            pass
        length = change_polymer(copy_file)
        if length < shortest_len:
            shortest_len = length
    return shortest_len


if __name__ == '__main__':
    print(remove_same_type())
