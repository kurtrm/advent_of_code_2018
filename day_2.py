"""
"""
from collections import Counter

from read_file import read_input


def checksum(filename):
    """
    """
    threes = 0
    twos = 0
    ids = read_input(filename)
    for label_id in ids:
        counts = {value: key for key, value in Counter(label_id).items()}
        try:
            counts[2]
            twos += 1
        except KeyError:
            pass
        try:
            counts[3]
            threes += 1
        except KeyError:
            pass

    return threes * twos


def differ():
    """
    """
    ids = read_input('input_2.txt')
    # correct_ids = []
    # for label_id in ids:
    #     counts = {value: key for key, value in Counter(label_id).items()}
    #     try:
    #         counts[2]
    #         correct_ids.append(label_id)
    #     except KeyError:
    #         pass
    #     try:
    #         counts[3]
    #         if correct_ids[-1] == label_id:
    #             continue
    #         correct_ids.append(label_id)
    #     except KeyError:
    #         pass

    for idx, first_label in enumerate(ids, 1):
        for second_label in ids[idx:]:
            total = 0
            for i, _ in enumerate(second_label):
                if first_label[i] != second_label[i]:
                    total += 1
            if total == 1:
                return first_label, second_label


if __name__ == '__main__':
    print(differ())
