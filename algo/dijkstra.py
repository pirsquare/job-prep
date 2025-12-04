import heapq

def dijkstra(graph, start_node):
    """
    Finds the shortest paths from a start_node to all other nodes in a graph.

    Args:
        graph (dict): An adjacency list representation of the graph.
                      Keys are nodes, values are dictionaries of neighbors
                      and their edge weights (e.g., {'A': {'B': 1, 'C': 4}}).
        start_node: The starting node for finding shortest paths.

    Returns:
        dict: A dictionary where keys are nodes and values are their shortest
              distances from the start_node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we found a shorter path to current_node already, skip this one
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example Usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
shortest_paths = dijkstra(graph, start)
print(f"Shortest paths from {start}: {shortest_paths}")

start = 'B'
shortest_paths = dijkstra(graph, start)
print(f"Shortest paths from {start}: {shortest_paths}")
