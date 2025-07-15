def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # Initialize the queue with the start node

    while queue:
        node = queue.pop(0)  # Dequeue a node (remove from the front of the list)
        
        if node not in visited:
            print(node, end=" ")  # Print the node
            visited.add(node)  # Mark the node as visited
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node
start_node = 'A'

# Call BFS function
print("Breadth-First Search starting from node", start_node, ":")
bfs(graph, start_node)
