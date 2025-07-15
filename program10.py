def printSolution(board):
    """Print the chessboard configuration."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n" + "-" * (len(board) * 2 - 1) + "\n")  # Separator between solutions

def isSafe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

def solveNQueens(board, row, n, solutions):
    """Use backtracking to solve the N-Queens problem and collect all solutions."""
    if row == n:
        # Store a copy of the current board configuration
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if isSafe(board, row, col, n):
            # Place the queen
            board[row][col] = 1
            # Recur to place the rest of the queens
            solveNQueens(board, row + 1, n, solutions)
            # Backtrack
            board[row][col] = 0

def nQueens(n):
    """Driver function to solve the N-Queens problem."""
    if n < 1:
        print("Board size must be at least 1.")
        return
    
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    solveNQueens(board, 0, n, solutions)
    
    if not solutions:
        print("No solution exists.")
    else:
        print(f"Found {len(solutions)} solutions for {n}x{n} board:")
        for i, sol in enumerate(solutions, 1):
            print(f"Solution {i}:")
            printSolution(sol)

# Solve the 8-Queens problem
N = 8
nQueens(N)