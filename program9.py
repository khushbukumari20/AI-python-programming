import math

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: leaf node reached
    if depth == 0 or node_index >= len(values):
        return values[node_index] if node_index < len(values) else float('-inf')
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):  # Each node has two children
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  # Each node has two children
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Example usage
if __name__ == "__main__":
    # Leaf node values for a complete binary tree
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth = 3  # Height of the tree (levels from root to leaf)
    optimal_value = alpha_beta_pruning(depth, 0, True, values, float('-inf'), float('inf'))
    print(f"The optimal value is: {optimal_value}")