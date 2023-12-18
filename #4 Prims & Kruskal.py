import time

# Prim's Algorithm
INF = 9999999
V = 5
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]
selected = [0, 0, 0, 0, 0]
no_edge = 0
selected[0] = True
start = time.time()
print("Edge : Weight\n")
while no_edge < V - 1:
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(f"{x}-{y} : {G[x][y]}")
    selected[y] = True
    no_edge += 1
end = time.time()
print("Execution Time for Prim's Algorithm:", (end - start) * 1000, "Milliseconds")

# Kruskal's Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [node for node in range(self.V)]
        rank = [0] * self.V
        start = time.time()
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        end = time.time()
        print("Edge : Weight")
        for u, v, w in result:
            print(f"{u}-{v} : {w}")
        print("Execution Time for Kruskal's Algorithm:", (end - start) * 1000, "Milliseconds")

# Example usage of Kruskal's Algorithm
V = 5
graph = Graph(V)
graph.add_edge(0, 1, 9)
graph.add_edge(0, 2, 75)
graph.add_edge(1, 2, 95)
graph.add_edge(1, 3, 19)
graph.add_edge(1, 4, 42)
graph.add_edge(2, 3, 51)
graph.add_edge(2, 4, 66)
graph.add_edge(3, 4, 31)
graph.kruskal()
