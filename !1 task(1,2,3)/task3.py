import math


def distance(x1, y1, x2, y2):

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


x1, y1 = 0, 0
x2, y2 = 1, 1
result = distance(x1, y1, x2, y2)
print(result)
