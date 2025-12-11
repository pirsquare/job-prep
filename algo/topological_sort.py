from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        """Add a directed edge from u to v. u must come before v."""
        self.graph[u].append(v)

    def topological_sort_dfs(self):
        visited = set()
        stack = deque() # Use deque for efficient appends/popleft

        # Helper recursive function for DFS
        def dfs_visit(node):
            visited.add(node)
            # Visit all neighbors
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_visit(neighbor)
            # Push current node to stack *after* all dependencies are visited
            stack.appendleft(node) # Use appendleft to build the correct order

        # Iterate over all vertices to cover disconnected components
        for i in range(self.V):
            if i not in visited:
                dfs_visit(i)

        # At this point, the stack contains the topological order
        return list(stack)
        # Or, if using a standard list and appending, return list(reversed(stack))

# Example Usage:
# Graph with 6 vertices: (5 -> 2), (5 -> 0), (4 -> 0), (4 -> 1), (2 -> 3), (3 -> 1)
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Following is a Topological Sort of the given graph:")
# A possible output is [5, 4, 2, 3, 1, 0] or [4, 5, 2, 3, 1, 0], etc.
# There can be multiple valid topological sorts.
print(g.topological_sort_dfs())
