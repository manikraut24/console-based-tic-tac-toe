#Create a Python console-based Tic Tac Toe game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 5)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))


def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, Enter Your Move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move. Please try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        move = get_move(current_player)
        row, col = divmod(move, 3)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("The cell is already taken. Try a different move.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break


if __name__ == "__main__":
    main()