
# dfs recursive approach
# recursive approach is simpler and cleaner
def dfs_recursive(graph, start_node, visited=set()):
    visited.add(start_node)
    print(start_node, end=" ")  # Process the node (e.g., print it)

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example Usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal (Recursive):")
dfs_recursive(graph, 'A')
# Expected Output: A B D E F C
print("")


# dfs interative approach using stack
# The iterative approach uses a stack to manage the nodes to be visited.
def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            print(current_node, end=" ") # Process the node

            # Add unvisited neighbors to the stack (order might affect traversal path slightly)
            # Reversing the neighbors ensures a consistent traversal order if desired
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example Usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nDFS Traversal (Iterative):")
dfs_iterative(graph, 'A')
# Expected Output: A B D E F C
print("")
