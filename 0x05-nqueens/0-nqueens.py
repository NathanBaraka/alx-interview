#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this column on the left side
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row, N, solutions):
    """Use backtracking to find all solutions."""
    if row >= N:
        # A valid solution was found, convert it to the required format
        solution = [[i, board[i].index(1)] for i in range(N)]
        solutions.append(solution)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1
            # Recur to place the rest of the queens
            solve_nqueens(board, row + 1, N, solutions)
            # Backtrack and remove the queen
            board[row][col] = 0

def main():
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate the input
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # List to hold all the solutions
    solutions = []
    
    # Solve the N Queens problem
    solve_nqueens(board, 0, N, solutions)
    
    # Print all the solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

