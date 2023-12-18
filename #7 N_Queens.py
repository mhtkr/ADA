import time

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

def solve_n_queens():
    n = int(input("Enter the number of queens: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    start_time = time.time()

    if not solve_n_queens_util(board, 0, n):
        print("No solution exists.")
        return

    end_time = time.time()
    execution_time = end_time - start_time

    print_board(board)
    print(f"Execution Time: {execution_time:.6f} seconds")

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

solve_n_queens()
