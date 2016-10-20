# Graph search: Strongly Connected Components

import sys
import threading

time = 0
source_vertex = 0
explored = None
finishing_time = None
leader = {}


def depth_first(r_graph, node):
    global time, finishing_time, explored

    explored[node] = True
    for to_node in r_graph[node]:
        if not explored[to_node]:
            depth_first(r_graph, to_node)

    time += 1
    finishing_time[time] = node


def depth_first_loop(graph, graph_len):
    global explored, finishing_time

    explored = [False] * graph_len
    finishing_time = [None] * graph_len

    for i in reversed(range(1, graph_len)):
        if not explored[i]:
            depth_first(graph, i)


def depth_first_leaders(graph, node):
    global leader, finishing_time, explored

    explored[node] = True
    leader[source_vertex] += 1
    for to_node in graph[node]:
        if not explored[to_node]:
            depth_first_leaders(graph, to_node)


def depth_first_loop_leaders(graph, graph_len):
    global leader, finishing_time, explored, source_vertex

    explored = [False] * graph_len

    for j in reversed(range(1, graph_len)):
        if not explored[finishing_time[j]]:
            source_vertex = finishing_time[j]
            leader[source_vertex] = 0
            depth_first_leaders(graph, finishing_time[j])


def count_scc(graph_len):
    global leader
    largest_scc = [0, 0, 0, 0, 0, 0]
    for i in range(graph_len):
        if i in leader:
            if leader[i] > largest_scc[5]:
                largest_scc[5] = leader[i]
                largest_scc.sort(reverse=True)
    return largest_scc[:5]


def read_input():
    g = {}
    rev_g = {}

    with open('SCC.txt') as f:
        for i in range(1, 875715):
            g[i] = []
            rev_g[i] = []
        for line in f:
            num1, num2 = line.split()
            v1 = int(num1)
            v2 = int(num2)
            g[v1].append(v2)
            rev_g[v2].append(v1)
    return g, rev_g


def main():
    print 'Running...'
    graph, rev_graph = read_input()
    depth_first_loop(rev_graph, len(graph) + 1)
    print 'Still running...'
    depth_first_loop_leaders(graph, len(graph) + 1)
    print count_scc(len(graph) + 1)
    print 'End'


if __name__=="__main__":
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()
