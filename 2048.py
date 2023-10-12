import random

# Initialize the game board
def initialize_board(size):
    board = [[0] * size for _ in range(size)]
    return board

# Add a new tile (2 or 4) to the board
def add_tile(board):
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

# Display the game board
def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))
    print()

# Check if the game is over
def is_game_over(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
            if j < len(board[i]) - 1 and board[i][j] == board[i][j + 1]:
                return False
            if i < len(board) - 1 and board[i][j] == board[i + 1][j]:
                return False
    return True

# Perform a move (left, right, up, or down)
def perform_move(board, direction):
    size = len(board)
    moved = False
    
    if direction == 'left':
        for i in range(size):
            board[i] = merge_tiles(board[i])
            if board[i] != [0] * size:
                moved = True
                
    elif direction == 'right':
        for i in range(size):
            board[i] = merge_tiles(board[i][::-1])[::-1]
            if board[i] != [0] * size:
                moved = True
                
    elif direction == 'up':
        for j in range(size):
            column = [board[i][j] for i in range(size)]
            merged_column = merge_tiles(column)
            for i in range(size):
                board[i][j] = merged_column[i]
            if column != [0] * size:
                moved = True
                
    elif direction == 'down':
        for j in range(size):
            column = [board[i][j] for i in range(size)][::-1]
            merged_column = merge_tiles(column)
            for i in range(size):
                board[i][j] = merged_column[::-1][i]
            if column != [0] * size:
                moved = True
                
    return moved

# Merge tiles in a row or column
def merge_tiles(line):
    size = len(line)
    merged_line = [0] * size
    index = 0
    
    for i in range(size):
        if line[i] != 0:
            if merged_line[index] == 0:
                merged_line[index] = line[i]
            elif merged_line[index] == line[i]:
                merged_line[index] *= 2
                index += 1
            else:
                index += 1
                merged_line[index] = line[i]
    return merged_line

# Main game loop
def play_game(size):
    board = initialize_board(size)
    add_tile(board)
    add_tile(board)
    
    while True:
        print_board(board)
        
        if is_game_over(board):
            print("Game over!")
            break
        
        direction = input("Enter move (left, right, up, down): ").lower()
        
        if direction in ['left', 'right', 'up', 'down']:
            moved = perform_move(board, direction)
            if moved:
                add_tile(board)
        else:
            print("Invalid move! Use 'left', 'right', 'up', or 'down'.")

if __name__ == "__main__":
    size = 4  # Change this to adjust the board size (e.g., 4 for 4x4)
    play_game(size)
