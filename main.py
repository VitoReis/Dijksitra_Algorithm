from igraph import *
import matplotlib.pyplot as plt
import numpy

def main():
    graph = Graph.Read_Ncol("myGraph.ncol", names=True, weights='auto', directed=True)     # Lendo o grafo
    openVertices = []
    visited = []
    graph.vs['weight'] = 'i'
    cost = numpy.zeros((len(graph.vs), 2), str)  # Cria uma matriz

    i = 0
    for vertex in graph.vs:                     # Acha o vertice inicial, define os custos e os vertices abertos
        openVertices.append(vertex)
        cost[i][0] = vertex['name']
        cost[i][1] = 'i'                        # Define o custo dos vertices como infinito -> i
        if vertex['name'] == '1':
            firstVertex = vertex
            visited.append(vertex)
            openVertices.remove(vertex)
            cost[i][1] = '0'
        i += 1

    shortestPath = []
    for vertex in openVertices:
        shortestPath.append(graph.get_shortest_paths(firstVertex, to=vertex, weights=None, mode='out', output='vpath'))
        visited.append(vertex)

    print('*'*20 + '\n' + 'Vertex and Index' + '\n' + '*'*20)
    for vertex in graph.vs:
        print(f'Vertex: {vertex["name"]} Index: {vertex.index}')
    print('*'*20 + '\n')

    print('*'*20 + '\n' + 'All shortest paths by index' + '\n' + '*'*20)
    for paths in shortestPath:
        print(f'{paths}')
    print('*' * 20 + '\n')

    print('*'*20 + '\n' + 'Vertices and Weights' + '\n' + '*'*20)
    for x in range(0, len(graph.vs)):
        print(f'Vertex: {cost[x][0]} Weight: {cost[x][1]}')
    print('*'*20 + '\n')

    # for weights in graph.es:
    #     print(weights['weight'])
    #     cost[i][1] = weights['weight']

if __name__ == '__main__':
    main()