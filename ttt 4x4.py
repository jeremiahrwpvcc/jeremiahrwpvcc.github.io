def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 16)

def check_win(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(4):
        if all(board[row][col] == player for row in range(4)):
            return True
    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3]) == player or \
       (board[0][3] == player and board[1][2] == player and board[2][1] == player and board[3][0]) == player:
        return True
    return False

def get_move():
    """Gets a valid move from the player."""
    while True:
        try:
            move = int(input("Enter your move (1-16): ")) - 1
            if 0 <= move < 16:
                return move // 4, move % 4
            else:
                print("Invalid move. Please enter a number between 1 and 16.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
    """Plays a game of Tic Tac Toe."""
    board = [[" " for _ in range(4)] for _ in range(4)]
    current_player = "X"

    for _ in range(16):
        print_board(board)
        row, col = get_move()
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    play_tic_tac_toe()
