# Dijkstras Algorithm for Shortest Distance


vertices_sofar = [1]
distances = [0]*201
distances[0] = 0
paths = [None]*201
paths[0] = []
paths[1] = []


def dijkstras_num(tail, tup):
    return distances[tail] + tup[1]


def shortest_path(graph):
    while len(vertices_sofar) != 200:
        smallest_dijkstras = None
        min_edge = None
        for vertex in vertices_sofar:
            for edge in graph[vertex]:
                if not edge[0] in vertices_sofar:
                    if smallest_dijkstras is None:
                        smallest_dijkstras = dijkstras_num(vertex, edge)
                        min_edge = edge
                    else:
                        if dijkstras_num(vertex, edge) < smallest_dijkstras:
                            smallest_dijkstras = dijkstras_num(vertex, edge)
                            min_edge = edge
        vertices_sofar.append(min_edge[0])
        distances[min_edge[0]] = smallest_dijkstras
        paths[min_edge[0]] = paths[vertex][:]
        paths[min_edge[0]].append(min_edge[0])


def read_input():
    # graph index corresponds to vertex num
    graph = [None]*201

    with open('dijkstraData.txt') as f:
        temp = [line.split() for line in f]

        for line in temp:
            index = int(line[0])
            graph[index] = []
            for item in line[1:]:
                pair = tuple(map(int, item.split(',')))
                graph[index].append(pair)

    return graph


if __name__=="__main__":
    graph = read_input()
    shortest_path(graph)

    res = []
    desired = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for i in desired:
        res.append(str(distances[i]))
    print ','.join(res)
