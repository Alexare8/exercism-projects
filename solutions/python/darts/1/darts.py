def score(x, y):
    radius = (x*x + y*y) ** (1/2)
    if radius <= 1:
        return 10
    if radius <= 5:
        return 5
    if radius <= 10:
        return 1
    return 0