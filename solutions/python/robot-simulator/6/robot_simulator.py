from operator import add

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
STEP_OFFSET = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TURN_OFFSET = {"R": 1, "L": -1}


class Robot:
    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.direction = direction
        self.coordinates = x_pos, y_pos
                            
    def move(self, moves: str) -> None:
        for move in moves:
            if move == "A":
                self.coordinates = tuple(coord + step for coord, step in zip(self.coordinates, STEP_OFFSET[self.direction]))
            else:
                self.direction = (self.direction + TURN_OFFSET[move]) % 4