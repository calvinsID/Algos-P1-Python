# Karger Min Cut

import random
import copy
import math


def change_nodes(graph, node1, node2):
    for node in graph:
        for index, el in enumerate(graph[node]):
            if el == node2:
                graph[node][index] = node1
    return


def contract(graph, node1, node2):
    graph[node1] += graph[node2]
    del graph[node2]
    change_nodes(graph, node1, node2)
    graph[node1] = list(filter(lambda x: x != node1, graph[node1]))
    return graph


def find_min_cut(graph):
    if len(graph) == 2:
        return len(list(graph.values())[0])
    else:
        node1 = random.choice(list(graph.keys()))
        node2 = random.choice(graph[node1])
        find_min_cut(contract(graph, node1, node2))
        return len(list(graph.values())[0])


if __name__=="__main__":
    original_dict = {}

    with open('KargerMinCut.txt') as f:
        # turn input into list of lists
        polyShape = [map(int, line.split()) for line in f]

    for item in polyShape:
        original_dict[item[0]] = item[1:]

    num_of_nodes = len(original_dict)
    min_cuts = num_of_nodes * num_of_nodes
    repeat = int(round(num_of_nodes * num_of_nodes * math.log(num_of_nodes)))

    for i in range(repeat):
        dic = copy.deepcopy(original_dict)
        cuts = find_min_cut(dic)
        if cuts < min_cuts:
            min_cuts = cuts
            print min_cuts
