DIGITS = {(' || ', '_ _ ', ' || '): "0",
          ('    ', '    ', ' || '): "1",
          ('  | ', '___ ', ' |  '): "2",
          ('    ', '___ ', ' || '): "3",
          (' |  ', ' _  ', ' || '): "4",
          (' |  ', '___ ', '  | '): "5",
          (' || ', '___ ', '  | '): "6",
          ('    ', '_   ', ' || '): "7",
          (' || ', '___ ', ' || '): "8",
          (' |  ', '___ ', ' || '): "9"
        }


def convert(input_grid: list[str]) -> str:
    """Decode a series of numbers encoded as 3 x 4 grids of pipes, underscores, and spaces."""
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    
    output = ""
    if not input_grid:
        return output
    
    for i in range(0, len(input_grid), 4):
        if output:
            output += ","
    
        rotated_grid = [''.join(column) for column in zip(*input_grid[i: i + 4])]
        for j in range(0, len(rotated_grid), 3):
            pattern = tuple(rotated_grid[j: j + 3])
            output += DIGITS.get(pattern, "?")
        
    return output
