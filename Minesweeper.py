import random

def initialize_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly on the board
    for _ in range(mines):
        while True:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            if board[row][col] != 'X':
                board[row][col] = 'X'
                break

    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_mines_around_cell(board, row, col):
    mine_count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'X':
            mine_count += 1

    return mine_count

def reveal_cell(board, revealed, row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == ' ':
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                reveal_cell(board, revealed, r, c)

def play_game(rows, cols, mines):
    board = initialize_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    game_over = False

    while not game_over:
        print_board(revealed)

        row = int(input("Enter row: "))
        col = int(input("Enter column: "))

        if board[row][col] == 'X':
            print("Game Over! You hit a mine.")
            game_over = True
        else:
            num_mines = count_mines_around_cell(board, row, col)
            revealed[row][col] = True
            if num_mines == 0:
                reveal_cell(board, revealed, row, col)

        if all(revealed[i][j] or board[i][j] == 'X' for i in range(rows) for j in range(cols)):
            print("Congratulations! You won!")
            game_over = True

if __name__ == "__main__":
    rows = 5
    cols = 5
    mines = 5
    play_game(rows, cols, mines)