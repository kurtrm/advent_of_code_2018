"""
"""
from datetime import datetime
from itertools import groupby

from read_file import read_input


def read_and_sort():
    """
    """
    file = read_input('input_4.txt')[:-1]
    sorted_logs = sorted(file, key=lambda x: datetime.strptime(x[1:17],
                                                               '%Y-%m-%d %H:%M'))
    records = [(datetime.strptime(event[1:11], '%Y-%m-%d'), event[12:17], event[19:]) for event in sorted_logs]
    grouped_records = groupby(records, lambda x: x[0])
    return grouped_records


def get_activity():
    """
    """
    guards = {}
    grouped_records = read_and_sort()
    for day, times in grouped_records:
        for event in times:
            if event[2].startswith('G'):
                guard_id = int(''.join(x for x in event[2][7:13] if x.isdigit()))
            elif event[2].startswith('f'):
                sleep_start = int(event[1][3:])
            else:
                sleep_end = int(event[1][3:])
                try:
                    for x in range(sleep_start, sleep_end):
                        guards[guard_id][x] += 1
                except KeyError:
                    guards[guard_id] = {i: 0 for i in range(0, 60)}
                    for x in range(sleep_start, sleep_end):
                        guards[guard_id][x] += 1
    return guards


def sleepiest_guard_and_minute():
    """
    """
    guards_sleep = get_activity()
    best_min = 0
    top_guard = None
    for key, value in guards_sleep.items():
        highest = sum(value.values())
        if highest > best_min:
            top_guard = key
    highest_count = 0
    highest_min = 0
    for key, value in guards_sleep[top_guard].items():
        if value > highest_count:
            highest_count = value
            highest_min = key

    return top_guard, highest_min


def sleepiest_minute():
    """
    """
    guards_sleep = get_activity()
    best_counts = 0
    best_min = 0
    top_guard = None
    for key, value in guards_sleep.items():
        top_counts = 0
        top_min = 0
        for minute, count in value.items():
            if count > top_counts:
                top_counts = count
                top_min = minute
        if top_counts > best_counts:
            top_guard = key
            best_counts = top_counts
            best_min = top_min

    return top_guard, best_min


if __name__ == '__main__':

    print(sleepiest_guard_and_minute())
    print(sleepiest_minute())
