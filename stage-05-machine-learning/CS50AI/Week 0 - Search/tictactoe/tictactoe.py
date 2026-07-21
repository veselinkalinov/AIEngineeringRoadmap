"""
Tic-Tac-Toe Player
"""

import copy

X = "X"
O = "O"  # noqa: E741
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count == o_count:
        return X

    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (
        not isinstance(action, tuple)
        or len(action) != 2
        or not all(isinstance(value, int) for value in action)
    ):
        raise ValueError("Action must be a tuple containing two integers.")

    i, j = action

    if i not in range(3) or j not in range(3):
        raise ValueError("Action is outside the board.")

    if board[i][j] is not EMPTY:
        raise ValueError("Cell is already occupied.")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    for column in range(3):
        lines.append([board[row][column] for row in range(3)])

    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] is not EMPTY and line[0] == line[1] == line[2]:
            return line[0]

    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1

    if game_winner == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_score = float("-inf")
        best_action = None
        alpha = float("-inf")
        beta = float("inf")

        for action in sorted(actions(board)):
            score = min_value(result(board, action), alpha, beta)

            if score > best_score:
                best_score = score
                best_action = action

            alpha = max(alpha, best_score)

            if best_score == 1:
                break

        return best_action

    best_score = float("inf")
    best_action = None
    alpha = float("-inf")
    beta = float("inf")

    for action in sorted(actions(board)):
        score = max_value(result(board, action), alpha, beta)

        if score < best_score:
            best_score = score
            best_action = action

        beta = min(beta, best_score)

        if best_score == -1:
            break

    return best_action


def max_value(board, alpha, beta):
    """
    Returns the maximum utility obtainable from the board.
    """
    if terminal(board):
        return utility(board)

    value = float("-inf")

    for action in actions(board):
        value = max(value, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, value)

        if alpha >= beta:
            break

    return value


def min_value(board, alpha, beta):
    """
    Returns the minimum utility obtainable from the board.
    """
    if terminal(board):
        return utility(board)

    value = float("inf")

    for action in actions(board):
        value = min(value, max_value(result(board, action), alpha, beta))
        beta = min(beta, value)

        if alpha >= beta:
            break

    return value
