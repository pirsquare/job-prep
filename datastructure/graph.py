

# adjacency list
# most common
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}



# adjacency matrix
# most common and simplest concept to store an adjacency matrix is to use a 2D array, which in python corresponds to nested lists
def create_adjacency_matrix(edges, num_nodes):
    # Initialize an N x N matrix with zeros
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    # For each edge (u, v), set the corresponding matrix cells to 1
    for u, v in edges:
        if 0 <= u < num_nodes and 0 <= v < num_nodes:
            matrix[u][v] = 1
            matrix[v][u] = 1 # For undirected graphs, the matrix is symmetric
        else:
            print(f"Error: Edge ({u}, {v}) is out of node range.")

    return matrix

# Example Usage:
# Graph with 4 nodes (0, 1, 2, 3) and edges (0, 1), (0, 2), (1, 2), (1, 3)
edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
num_nodes = 4
adj_matrix = create_adjacency_matrix(edges, num_nodes)

print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Output:
# Adjacency Matrix:
# [0, 1, 1, 0]
# [1, 0, 1, 1]
# [1, 1, 0, 0]
# [0, 1, 0, 0]



# WeightedGraph in adjacency list
class WeightedGraph:
    def __init__(self):
        # Graph stored as a dictionary: {node: [(neighbor, weight), ...]}
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, weight):
        # Adds an edge from u to v with weight e
        if u not in self.graph:
            self.add_node(u)
        if v not in self.graph:
            self.add_node(v)

        # For an undirected graph, add connection in both directions
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight)) # Remove this line for a directed graph

    def get_neighbors_with_weights(self, node):
        return self.graph.get(node, [])

# Example Usage:
g = WeightedGraph()
g.add_edge('A', 'B', 10)
g.add_edge('A', 'C', 5)
g.add_edge('B', 'C', 3)

print(f"Neighbors of A: {g.get_neighbors_with_weights('A')}")
print(f"Neighbors of B: {g.get_neighbors_with_weights('B')}")
