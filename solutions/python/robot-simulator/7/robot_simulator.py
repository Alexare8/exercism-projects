NORTH = complex(0, 1)
EAST = complex(1, 0)
SOUTH = complex(0, -1)
WEST = complex(-1, 0)
TURN = {"L": 1j, "R": -1j}


class Robot:
    def __init__(self, direction: complex = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.direction = direction
        #Internally store location as complex
        self.position = complex(x_pos, y_pos)

    @property
    def coordinates(self) -> tuple[int, int]:
        #Externally display location as 2-tuple
        return int(self.position.real), int(self.position.imag)
                            
    def move(self, moves: str) -> None:
        for move in moves:
            if move == "A":
                self.position += self.direction
            else:
                self.direction *= TURN[move]
