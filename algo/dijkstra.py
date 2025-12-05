import heapq




def dijkstra(graph, start_node):
    """
    Core Idea:
    Initialize: Start with the source node having a distance of 0 and all other nodes having an "infinite" distance.
    Explore: Repeatedly select the unvisited node with the smallest known distance.
    Update Neighbors: For the selected node, examine its unvisited neighbors. If a shorter path to a neighbor is found through the current node, update the neighbor's distance.
    Mark Visited: Mark the current node as visited.
    Repeat: Continue until all reachable nodes are visited.

    Explanation of the Code:
    heapq: Used to implement a min-priority queue, efficiently retrieving the unvisited node with the smallest distance.

    distances dictionary: Stores the shortest distance found so far from start_node to each node.

    priority_queue: Stores tuples of (distance, node). heapq.heappop always retrieves the tuple with the smallest distance.

    current_distance > distances[current_node] check: Prevents reprocessing nodes if a shorter path has already been found and processed.

    Neighbor exploration: Iterates through the neighbors of the current_node and calculates the distance to them through the current_node.

    Distance Update: If a new distance to a neighbor is shorter than its currently recorded distances[neighbor], it's updated, and the neighbor is added to the priority_queue with its new distance.

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

    # priority_queue = []  # (distance, node)
    # for node, distance in distances.items():
    #     priority_queue.append((distance, node))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we found a shorter path to current_node already, skip this one
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distances[neighbor] > distance:
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
