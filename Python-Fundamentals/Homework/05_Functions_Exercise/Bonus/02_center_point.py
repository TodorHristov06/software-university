import math

def closest_to_center(x1, y1, x2, y2):
    #we calculate the hypotenuse of a triangle a^2 + b^2 = c^2
    dist1 = math.sqrt(x1**2 + y1**2)
    dist2 = math.sqrt(x2**2 + y2**2)
    
    if dist1 <= dist2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest_to_center(x1, y1, x2, y2)