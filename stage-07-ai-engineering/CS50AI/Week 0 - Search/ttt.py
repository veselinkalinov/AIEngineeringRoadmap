def print_board(board):
    print()
    for row in range(3):
        print(" | ".join(board[row * 3 : row * 3 + 3]))
        if row < 2:
            print("--+---+--")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    return any(
        board[a] == board[b] == board[c] == player for a, b, c in winning_combinations
    )


def main():
    board = [str(number) for number in range(1, 10)]
    current_player = "X"

    print("Tic-Tac-Toe")
    print("Choose a position from 1 to 9.")

    for turn in range(9):
        print_board(board)

        while True:
            move = input(f"Player {current_player}, choose a position: ")

            if not move.isdigit():
                print("Enter a number from 1 to 9.")
                continue

            position = int(move) - 1

            if position not in range(9):
                print("Enter a number from 1 to 9.")
                continue

            if board[position] in ("X", "O"):
                print("That position is already taken.")
                continue

            break

        board[position] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    main()
