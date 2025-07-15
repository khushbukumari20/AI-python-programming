from collections import deque

def bfs(start_state):
    # Target state: 3x3 grid in solved order with 0 as the empty space
    target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    dq = deque([start_state])
    visited = {tuple(start_state): None}  # Use tuple as key for hashability
    
    while dq:
        state = dq.popleft()
        if state == target:
            # Reconstruct the path
            path = []
            while state:
                path.append(state)
                state = visited[tuple(state)]
            return path[::-1]  # Reverse to get path from start to target
        
        # Find the position of the empty space (0)
        zero = state.index(0)
        row, col = divmod(zero, 3)
        
        # Possible moves: up (-3), down (+3), left (-1), right (+1)
        for move in (-3, 3, -1, 1):
            # Calculate new position
            new_pos = zero + move
            new_row, new_col = divmod(new_pos, 3)
            
            # Check if the move is valid (within bounds and adjacent)
            if (0 <= new_row < 3 and 0 <= new_col < 3 and 
                abs(row - new_row) + abs(col - new_col) == 1):
                # Create a new state by swapping 0 with the neighbor
                neighbor = state[:]
                neighbor[zero], neighbor[new_pos] = neighbor[new_pos], neighbor[zero]
                
                if tuple(neighbor) not in visited:
                    visited[tuple(neighbor)] = state
                    dq.append(neighbor)
    
    return None  # Return None if no solution is found

def printSolution(path):
    if path:
        for state in path:
            # Print each state as a 3x3 grid
            print("\n".join(" ".join(map(str, state[i:i+3])) for i in range(0, 9, 3)), end="\n-----\n")
    else:
        print("No solution to display.")

# Example Usage
start_state = [1, 3, 0, 6, 8, 4, 7, 5, 2]
solution = bfs(start_state)

if solution:
    printSolution(solution)
    print(f"Solved in {len(solution) - 1} moves.")
else:
    print("No solution found.")