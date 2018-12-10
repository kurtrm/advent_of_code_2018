"""
dicty = {
     'C': {
         'A': {'B': {E: {}, 'D': {'E': {}}}, 'F':{'E': {}}}}}
"""
from read_file import read_input
import heapq


def extract_pairs():
    """
    """
    lines = read_input('input_7.txt')[:-1]
    all_pairs = [(line[5], line[-12]) for line in lines]
    return all_pairs


def construct_tree():
    """
    """
    graph = {}
    pairs = extract_pairs()
    for first, second in pairs:
        try:
            node = graph[first]
            node.append(second)
        except KeyError:
            graph[first] = [second]
        try:
            graph[second]
        except KeyError:
            graph[second] = []
    reverse_dict = {}
    keys = graph.keys()
    for key in graph:
        graph[key] = sorted(graph[key])
    for this_step in keys:
        reverse_dict[this_step] = []
        for key, val in graph.items():
            if this_step in val:
                reverse_dict[this_step].append(key)
    in_degree = {node: len(val) for node, val in reverse_dict.items()}
    stack = [(node, node) for node in in_degree if in_degree[node] == 0]
    for node in stack:
        in_degree[node[1]] -= 1
    heapq.heapify(stack)
    topography = []
    while stack:
        _, zero = heapq.heappop(stack)
        topography.append(zero)
        for node in graph[zero]:
            in_degree[node] -= 1
        for node, val in in_degree.items():
            if val == 0:
                heapq.heappush(stack, (node, node))
                in_degree[node] -= 1
    return ''.join(topography)


if __name__ == '__main__':
    print(construct_tree())
