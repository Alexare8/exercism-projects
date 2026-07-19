NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos) 

    def move(self, moves):
        for move in moves:
            if move == "A":
                  print(self.direction)
                  self.coordinates = (self.coordinates[0] + self.direction[0], self.coordinates[1] + self.direction[1])
                  continue
            elif move == "R":
                turn = 1
            elif move == "L":
                turn = -1
            self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) + turn) % 4]