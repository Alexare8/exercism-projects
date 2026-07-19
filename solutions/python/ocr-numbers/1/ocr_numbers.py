DIGITS = [([' || ', '_ _ ', ' || '], "0"),
          (['    ', '    ', ' || '], "1"),
          (['  | ', '___ ', ' |  '], "2"),
          (['    ', '___ ', ' || '], "3"),
          ([' |  ', ' _  ', ' || '], "4"),
          ([' |  ', '___ ', '  | '], "5"),
          ([' || ', '___ ', '  | '], "6"),
          (['    ', '_   ', ' || '], "7"),
          ([' || ', '___ ', ' || '], "8"),
          ([' |  ', '___ ', ' || '], "9")
          ]


def convert(input_grid: list[str]) -> str:
    """Decode a series of numbers encoded as 3 x 4 grids of pipes, underscores, and spaces."""
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    
    output = ""
    if not input_grid:
        return output
    
    for i in range(len(input_grid) // 4):
        if output:
            output += ","
    
        rotated_grid = [''.join(column) for column in zip(*input_grid[4 * i: 4 * i + 4])]
        for j in range(len(rotated_grid) // 3):
            output += decode_char(rotated_grid[3 * j: 3 * j+3])
        
    return output


def decode_char(rotated_grid: list[str]) -> str:
    """Given a 3 x 4 grid of pipes, underscores, and spaces, determine which number is represented, or whether it is garbled."""
    for digit in DIGITS:
        if all(rotated_grid[i] == column for i, column in enumerate(digit[0])):
            return digit[1]
    return "?"
