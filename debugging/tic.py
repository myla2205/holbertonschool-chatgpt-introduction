#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    winner = None

    while winner is None and not is_board_full(board):
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(
                input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Please enter 0, 1, or 2 for both row and column.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                winner = check_winner(board)
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")


tic_tac_toe()
