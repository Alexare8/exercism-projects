"""
Evaluate the state of a Tic Tac Toe game board.

Accepts game boards as lists of lists of "X", "O", and "".
"""

def gamestate(board: list[str]) -> str:
    """Evaluate the game state as win, draw, or onging."""
    flat_board = "".join(board)
    total_x = flat_board.count("X")
    total_o = flat_board.count("O")
    if total_x - total_o > 1:
        raise ValueError("Wrong turn order: X went twice")
    if total_o > total_x:
        raise ValueError("Wrong turn order: O started")

    x_win, o_win = detect_wins(board)
    if x_win and o_win:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if not x_win | o_win:
        if total_x + total_o == 9:
            return "draw"
        return "ongoing"

    return "win"


def detect_wins(board: list[str]) -> tuple[bool, bool]:
    """Determine which if either player has a win present on the board."""
    top_row, mid_row, bottom_row = board
    left_col, mid_col, right_col = ["".join(row) for row in zip(*board)]
    first_diag = "".join([board[0][0], board[1][1], board[2][2]])
    second_diag = "".join([board[0][2], board[1][1], board[2][0]])

    x_win = False
    o_win = False
    for slot in [top_row, mid_row, bottom_row,
            left_col, mid_col, right_col,
            first_diag, second_diag]:
        if slot == "XXX":
            x_win = True
        elif slot == "OOO":
            o_win = True
    return (x_win, o_win)
