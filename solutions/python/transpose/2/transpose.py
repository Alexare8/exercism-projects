def transpose(lines: str) -> str:
    """Transpose strings."""
    if not lines:
        return ''
    lines_split = lines.split('\n')
    longest = max(len(line) for line in lines_split)
    lines_split = [line.ljust(longest, '_') for line in lines_split]
    return '\n'.join(
        ''.join(line[i] for line in lines_split).rstrip('_').replace('_', ' ') 
        for i in range(longest)
    )
