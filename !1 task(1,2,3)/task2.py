import math


def square_properties(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side

    return perimeter, area, diagonal


side_length = 7
properties = square_properties(side_length)

print("Периметр:", properties[0])
print("Площадь:", properties[1])
print("Диагональ:", properties[2])
