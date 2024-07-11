def is_valid_triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    
    return sides[0] + sides[1] > sides[2]

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))
