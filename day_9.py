"""
"""
from itertools import cycle
from collections import defaultdict

# if __name__ == '__main__':
"""
466 players; last marble is worth 71436
"""
    # import sys
    # i = 3
    # idx = 1
    # players = cycle(range(1, int(sys.argv[1])+1))
    # next(players)
    # next(players)
    # listy = [0, 2, 1]
    # scores = defaultdict(int)
    # while i < (int(sys.argv[2])+1):
    #     curr_player = next(players)
    #     next_idx = idx + 2
    #     if i % 23 == 0:
    #         scores[curr_player] += i
    #         back_idx = idx - 7
    #         if back_idx < 0:
    #             back_idx = len(listy) + back_idx
    #         back_marble = listy.pop(back_idx)
    #         scores[curr_player] += back_marble
    #         idx = back_idx
    #     elif next_idx == len(listy):
    #         listy.append(i)
    #         idx = next_idx  # [0, 2, 1, 3]
    #     elif next_idx > len(listy):
    #         idx = 1
    #         listy.insert(idx, i)
    #     else:
    #         listy.insert(next_idx, i)
    #         idx = next_idx
    #     i += 1
    # print(max(scores.items(), key=lambda x: x[1])[1])
    # import sys
# def scores():
#     i = 3
#     idx = 1
#     players = cycle(range(1, 467))
#     next(players)
#     next(players)
#     listy = [0, 2, 1]
#     scores = defaultdict(int)
#     top_scores = []
#     while i < 71437:
#         curr_player = next(players)
#         next_idx = idx + 2
#         if i % 23 == 0:
#             scores[curr_player] += i
#             back_idx = idx - 7
#             if back_idx < 0:
#                 back_idx = len(listy) + back_idx
#             back_marble = listy.pop(back_idx)
#             scores[curr_player] += back_marble
#             idx = back_idx
#         elif next_idx == len(listy):
#             listy.append(i)
#             idx = next_idx  # [0, 2, 1, 3]
#         elif next_idx > len(listy):
#             idx = 1
#             listy.insert(idx, i)
#         else:
#             listy.insert(next_idx, i)
#             idx = next_idx
#         i += 1
#         if i > 23:
#             top_scores.append((i, max(scores.items(), key=lambda x: x[1])[1]))
#     return top_scores


# def mod_scores():
#     i = 3
#     idx = 1
#     players = cycle(range(1, 467))
#     next(players)
#     next(players)
#     listy = [0, 2, 1]
#     scores = defaultdict(int)
#     top_scores = []
#     while i < 71437:
#         curr_player = next(players)
#         next_idx = idx + 2
#         if i % 23 == 0:
#             scores[curr_player] += i
#             back_idx = idx - 7
#             if back_idx < 0:
#                 back_idx = len(listy) + back_idx
#             back_marble = listy.pop(back_idx)
#             scores[curr_player] += back_marble
#             idx = back_idx
#         elif next_idx == len(listy):
#             listy.append(i)
#             idx = next_idx  # [0, 2, 1, 3]
#         elif next_idx > len(listy):
#             idx = 1
#             listy.insert(idx, i)
#         else:
#             listy.insert(next_idx, i)
#             idx = next_idx
#         i += 1
#         if i > 23:
#             try:
#                 top_scores.append(scores[94])
#             except IndexError:
#                 top_scores.append(0)
#     return top_scores

class Node:
    """
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    """
    466 players; last marble is worth 71436
    """
    import sys
    i = 3
    idx = 1
    # players = cycle(range(1, int(sys.argv[1])+1))
    node = Node(0)
    node.right = Node(2)
    node.right.right = Node(1)
    node.right.left = node
    node.right.right.left = node.right
    node.left = node.right.right
    curr_node = node
    for _ in range(3):
        print(curr_node.value)
        curr_node = curr_node.right
    curr_node = node
    for _ in range(3):
        print(curr_node.value)
        curr_node = curr_node.left
