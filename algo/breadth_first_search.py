from collections import deque

def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque()  # Queue to be visited BFS traversal

    # Add the start node to the queue and mark as visited
    queue.append(start_node)
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()  # Dequeue a node
        print(current_node, end=" ")  # Process the current node

        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example Usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal starting from 'A':")
bfs(graph, 'A')
