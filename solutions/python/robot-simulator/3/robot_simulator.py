from operator import add

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
TURN_DICT = {"R": 1, "L": -1}


class Robot:
    def __init__(self, direction=NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.direction = direction
        self.coordinates = (x_pos, y_pos) 

    def move(self, moves: str) -> None:
        for move in moves:
            if move == "A":
                self.coordinates = tuple(map(add, self.coordinates, self.direction))
                #self.coordinates = (self.coordinates[0] + self.direction[0], self.coordinates[1] + self.direction[1])
            else:
                self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) + TURN_DICT[move]) % 4]