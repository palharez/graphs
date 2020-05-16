# Python Program to detect cycle in an undirected graph
from collections import defaultdict


class Graph:
    # This class represents a undirected graph using adjacency list representation

    def __init__(self, vertices, graph):
        self.V = vertices  # No. of vertices
        self.graph = graph  # default dictionary to store graph

    # A recursive function that uses visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False

    # Returns true if the graph contains a cycle, else false.
    def isCyclic(self):
        # Mark all the vertices as not visited
        visited = [False] * (self.V)
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if visited[i] == False:  # Don't recur for u if it is already visited
                if(self.isCyclicUtil(i, visited, -1)) == True:
                    return True
        return False


def main():
    """
    Um ciclo é formado da seguinte maneira
    Se o vértice 'v', for adjacente a 'u', e 'u' for um vértice
    já visitado e não for parent de v, temos um cycle graph
     0 -> 1 -> 2 -> 0
         0
        / \
       1 - 2
    """
    _g = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2]
    }

    _g = {
        0: [1, 0, 0],
        1: [0]
    }

    n = 4

    g = Graph(n, _g)

    print(g.isCyclic())


if __name__ == "__main__":
    main()
