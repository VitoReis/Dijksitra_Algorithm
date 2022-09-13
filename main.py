from igraph import *
import matplotlib.pyplot as plt
import numpy
import numpy as np

def main():
    graph = Graph.Read_Ncol("myGraph.ncol", names=True, weights='auto', directed=True)     # Lendo o grafo
    openVertices = []
    visited = []
    graph.vs['dist'] = np.inf
    currentVertex = None

    for vertex in graph.vs:                     # Define todos os vertices como abertos e com valor infinito
        openVertices.append(vertex)
        graph.vs[vertex.index]['dist'] = np.inf

    first = True
    while len(openVertices) > 0:
        if first:                           # Define o vertice de index 0 como o primeiro a rodar
            graph.vs[0]['dist'] = 0
            currentVertex = graph.vs[0]
            first = False
        else:                               # Encontra o vertice atual
            smaller = np.inf
            for vertex in graph.vs:
                if vertex in openVertices and graph.vs[vertex.index]["dist"] <= smaller:
                    currentVertex = vertex
                    smaller = graph.vs[vertex.index]["dist"]

        visited.append(currentVertex)
        openVertices.remove(currentVertex)
        s = []

        for vertex in openVertices:
            if vertex.index in graph.neighbors(currentVertex, mode='out'):
                s.append(vertex)


        for v in range(0, len(s)):
            p = np.inf
            if len(s) >= 2:
                p = graph.es.select(_source=currentVertex.index,_target=s[v].index)['weight'][0]
            if p < graph.vs[s[v].index]["dist"]:
                graph.vs[s[v].index]["dist"] = p + currentVertex['dist']
        currentVertex = None


    print('*' * 19 + '\n' + '* Vertex * Weight *' + '\n' + '*' * 19)
    for vertex in graph.vs:
        print(f'   {graph.vs[vertex.index]["name"]}         {graph.vs[vertex.index]["dist"]}')
    print('*' * 19)



if __name__ == '__main__':
    main()