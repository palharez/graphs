class Vertex:
	def __init__(self, n):
		self.name = n

class Graph:
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

            for row in self.edges:
                row.append(0)

            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)

    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {}

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight


def findJudge(n, trust):

    # Creating graph
    g = Graph()

    for z in range(n):
        vert = Vertex(z + 1)
        g.add_vertex(vert)
    
    # Creating edges
    for a, b in trust:
        g.add_edge(a, b)

    judge = {}

    for vertex in g.vertices.keys():
        indice = g.edge_indices.get(vertex)

        # Column
        trusts = 0
        for k in range(len(g.edges)):
            trusts += g.edges[k][indice]

        # Line
        entrusts = 0
        for j in range(len(g.edges)):
            entrusts += g.edges[indice][j]

        if not entrusts and trusts and trusts == len(g.vertices.keys()) - 1:
            if not judge:
                judge = {
                    'name': vertex,
                    'trusts': trusts
                }
            elif trusts > judge['trusts']:
                judge = {
                    'name': vertex,
                    'trusts': trusts
                }
            elif trusts == judge['trusts']:
                judge = {}

    return judge['name'] if judge else -1

def main():
    print(findJudge(n = 2, trust = [[1,2]]))
    print(findJudge(n = 3, trust = [[1,3],[2,3]]))
    print(findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))
    print(findJudge(n = 3, trust = [[1,2],[2,3]]))
    print(findJudge(n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))

if __name__ == "__main__":
    main()