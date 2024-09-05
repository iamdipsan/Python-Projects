def print_board(board):
    """Prints the game board in a structured format with borders."""
    print("\n+---+---+---+")  # Print the top border of the board
    for row in board:
        # print each row with cell values separated by borders
        print("| " + " | ".join(row) + " |")
        # print the border after each row
        print("+---+---+---+")

def check_winner(board):
    """Checks for a winner or a draw."""
    # define all possible winning lines: rows, columns, and diagonals
    lines = [
        [board[0][0], board[0][1], board[0][2]],  # Row 1
        [board[1][0], board[1][1], board[1][2]],  # Row 2
        [board[2][0], board[2][1], board[2][2]],  # Row 3
        [board[0][0], board[1][0], board[2][0]],  # Column 1
        [board[0][1], board[1][1], board[2][1]],  # Column 2
        [board[0][2], board[1][2], board[2][2]],  # Column 3
        [board[0][0], board[1][1], board[2][2]],  # Diagonal from top-left to bottom-right
        [board[0][2], board[1][1], board[2][0]]   # Diagonal from top-right to bottom-left
    ]

    # Check each line to see if all three cells are the same and not empty
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != ' ':
            return line[0]  # Return the player ('X' or 'O') who has won

    # Check if all cells are filled and there is no winner
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'  # Return 'Draw' if the board is full and no winner

    return None  # Return None if no winner and the game is not a draw

def main():
    """Main function to play the Tic Tac Toe game."""
    # Initialize the board with empty spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Start with player 'X'

    while True:
        print_board(board)  # Print the current state of the board

        try:
            # Prompt the current player for their move
            move = input(f"Player {current_player}, enter your move (1-9): ")
            move = int(move)  # Convert the input to an integer
            
            # Check if the move is valid (between 1 and 9)
            if move < 1 or move > 9:
                print("Invalid move, try again.")
                continue  # Ask for a new move

        except ValueError:
            # Handle cases where the input is not an integer
            print("Invalid move, try again.")
            continue  # Ask for a new move

        # Convert the move number to board coordinates (row, col)
        row, col = divmod(move - 1, 3)

        # Check if the cell is already occupied
        if board[row][col] != ' ':
            print("Cell already occupied. Choose a different cell.")
            continue  # Ask for a new move
        
        # Place the current player's mark on the board
        board[row][col] = current_player

        # Check if there is a winner or if the game is a draw
        winner = check_winner(board)

        if winner:
            print_board(board)  # Print the final board state
            if winner == 'Draw':
                print("The game is a draw!")
            else:
                print(f"Player {winner} wins!")  # Announce the winner
            break  # End the game

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()  # Start the game
