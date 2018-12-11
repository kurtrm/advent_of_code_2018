"""
"""
from read_file import read_input


# def parse_license():
#     """
#     """
#     raw_code = read_input('input_8.txt', ' ')
#     int_code = [int(num) for num in raw_code]
#     # int_code = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
#     total_nums = len(int_code)
#     i = 0
#     total_children = 1
#     metadata_sum = 0
#     while i < total_nums:
#         if total_children == 0:
#             remaining_meta = total_nums - i
#             for _ in range(remaining_meta):
#                 metadata_sum += int_code[i]
#                 i += 1
#         else:
#             total_children -= 1
#             total_children += int_code[i]
#             if int_code[i] == 0:
#                 i += 1
#                 num_meta = int_code[i]
#                 for _ in range(num_meta):
#                     i += 1
#                     metadata_sum += int_code[i]
#                 i += 1
#             else:
#                 i += 2

#     return metadata_sum


def parse_license(i, int_code):
    """
    """
    meta_sum = 0
    if int_code[i] == 0:
        i += 1
        local_meta_total = 0
        for _ in range(int_code[i]):
            i += 1
            local_meta_total += int_code[i]
        return i+1, local_meta_total
    meta_sigs = int_code[i+1]
    i += 2
    for _ in range(int_code[i-2]):
        i, local_meta = parse_license(i, int_code)
        # import pdb; pdb.set_trace()
        meta_sum += local_meta
    for _ in range(meta_sigs):
        meta_sum += int_code[i]
        i += 1
    if i >= len(int_code):
        return meta_sum
    return i, meta_sum


if __name__ == '__main__':
    raw_code = read_input('input_8.txt', ' ')
    int_code = [int(num) for num in raw_code]
    # int_code = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

    print(parse_license(0, int_code))
