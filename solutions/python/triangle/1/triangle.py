def equilateral(sides):
    return triangle(sides) and sides[0] == sides[1] == sides[2]
        

def isosceles(sides):
    return triangle(sides) and (sides[0] in sides[1:] or sides[1] == sides[2])


def scalene(sides):
    return triangle(sides) and sides[0] != sides[1] != sides[2] != sides[0]


def triangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b and 0 not in sides