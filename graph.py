import abc

import numpy as np

#################################################
# The base class representation of a gRaph with #
# all the interface methods                     #
#                                               #
#################################################

class Graph(abc.ABC):
    def __init__(self, numVertices, directed=False):
        self.numVertices  = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    #gets any adjacent node/vertex for a given node/vertex#
    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    #returns number of edges that are incident on a given vertex#
    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    #returns weight of edge connecting two nodes/vertices#
    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    #used to print out the graph, used for debugging#
    @abc.abstractmethod
    def display(self):
        pass



class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight

        #if graph is undirected then there needs to be a connection going the other way#
        if self.directed == False:
            self.matrix[v2][v1] = weight

    #return all vertices that flow into the vertex specified#
    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    #get indegree of given vertex#
    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "------>", v)

g = AdjacencyMatrixGraph(4, directed=True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

for i in range(4):
    print("Indegree: ", i, g.get_indegree(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

g.display()
