def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    
    visited.add(start)  # Mark the current node as visited
    print(start, end=" ")  # Print the current node
    
    # Recursively visit all unvisited neighbors of the node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

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

# Call DFS function
print("Depth-First Search starting from node", start_node, ":")
dfs(graph, start_node)
