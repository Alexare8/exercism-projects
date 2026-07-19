class Queen:
    def __init__(self, row: int, column: int):
        if validate_square(row, column):
            self.row, self.column = row, column

    def can_attack(self, another_queen) -> bool:
        """Determines if a chess queen is in position to attack another queen."""
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (self.row == another_queen.row or self.column == another_queen.column or
            abs(self.column - another_queen.column) == abs(self.row - another_queen.row))

def validate_square(row: int, column: int) -> bool:
    """Validate existance of chess square or raise ValueError"""
    if row < 0:
        raise ValueError("row not positive")
    if row > 7:
        raise ValueError("row not on board")
    if column < 0:
        raise ValueError("column not positive")
    if column > 7:
        raise ValueError("column not on board")
    return True