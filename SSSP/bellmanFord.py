# Python Implementation of Bellman-Ford Algorithm
from typing import List, Tuple


class BellmanFord:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []  # List to hold all edges (u, v, weight)

    def add_edge(self, u: int, v: int, weight: float):
        # Add an edge from vertex u to vertex v with given weight
        self.edges.append((u, v, weight))

    def bellman_ford(self, start: int) -> Tuple[List[float], bool]:
        #         # Initialize distances and parent pointers
        distance = [float('inf')] * self.vertices
        distance[start] = 0

        # Step 1: Relax all edges |V| - 1 times
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        # Step 2: Check for negative-weight cycles
        for u, v, weight in self.edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("Graph contains a negative-weight cycle")
                return distance, False  # Negative cycle detected

        return distance, True  # Returned with success


# Example usage:
if __name__ == "__main__":
    graph = BellmanFord(5)
    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)
    graph.add_edge(3, 2, 5)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 3, -3)

    start_vertex = 0
    distances, no_negative_cycle = graph.bellman_ford(start_vertex)

    if no_negative_cycle:
        print("Vertex distances from source:")
        for i, d in enumerate(distances):
            print(f"Distance to vertex {i}: {d}")