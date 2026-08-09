class ConnectGame:
    def __init__(self, board: str):
        self.board = board.replace(" ", "").split("\n")

    def get_winner(self) -> str:
        if self.search("X"):
            return "X"
        if self.search("O", transpose=True):
            return "O"
        return ""

    def search(self, player: str, transpose: bool=False) -> bool:
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
            visualize(board, x, y)
            print()
            if y == width - 1:
                return True
            for neighbor in self.get_neighbors(board, x, y):
                nx, ny = neighbor[0], neighbor[1]
                if neighbor not in searched and board[nx][ny] == player:
                    searched.append(neighbor)
                    queue.append(neighbor)

        return False

    @staticmethod
    def get_neighbors(board: list[str], x, y: int) -> list[tuple[int, int]]:
        potential_neighbors =  [
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
        ]

        valid_neighbors = []
        for x, y in potential_neighbors:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                valid_neighbors.append((x, y))

        return valid_neighbors

def visualize(board: list[str], x, y: int) -> None:
    for i, row in enumerate(board):
        if x == i:
            row = row + " "
            print(f"{row[:y]}\033[0;47m{row[y]}\033[0m{row[y+1:]}")
        else:
            print(row)
