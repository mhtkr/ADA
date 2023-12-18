import time

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        spt_set = [False] * self.V
        start = time.time()

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if not spt_set[v] and self.graph[u][v] and dist[u] != float('inf') and (dist[u] + self.graph[u][v] < dist[v]):
                    dist[v] = dist[u] + self.graph[u][v]

        end = time.time()
        self.print_solution(dist)
        print("Execution Time for Dijkstra's Algorithm:", (end - start) * 1000, "Milliseconds")

    def min_distance(self, dist, spt_set):
        min_dist = float('inf')
        min_index = -1

        for v in range(self.V):
            if not spt_set[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v

        return min_index

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

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
src = 0
graph.dijkstra(src)
