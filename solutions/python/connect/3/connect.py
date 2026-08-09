class ConnectGame:
    def __init__(self, board: str):
        self.board = board.replace(" ", "").split("\n")

    def get_winner(self) -> str:
        """Determine which player if either has won the game."""
        if self.search("X"):
            return "X"
        if self.search("O", transpose=True):
            return "O"
        return ""

    def search(self, player: str, transpose: bool=False) -> bool:
        """Determine if an unbroken line of player's pieces crosses the board."""
        board = self.board
        width = len(self.board[0])
        height = len(self.board)
        if transpose:
            board = ["".join(row) for row in zip(*board)]
            width, height = height, width

        searched = []
        queue = []
        for i in range(height):
            if board[i][0] == player:
                searched.append((i, 0))
                queue.append((i, 0))

        while queue:
            x, y = queue.pop(0)
            if y == width - 1:
                return True
            for nx, ny in self.get_neighbors(x, y, height, width):
                if (nx, ny) not in searched and board[nx][ny] == player:
                    searched.append((nx, ny))
                    queue.append((nx, ny))

        return False

    @staticmethod
    def get_neighbors(x, y, height, width: int) -> list[tuple[int, int]]:
        """List the neighbors of (X, Y) on a hexagonal grid of given height and width."""
        potential_neighbors =  [
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
        ]

        valid_neighbors = []
        for px, py in potential_neighbors:
            if 0 <= px < height and 0 <= py < width:
                valid_neighbors.append((px, py))

        return valid_neighbors
