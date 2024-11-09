from math import pi


shape = input()

if shape == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")
    
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
    
elif shape == "circle":
    radius = float(input())
    area = radius * radius * pi
    print(f"{area:.3f}")
    
elif shape == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height) / 2
    print(f"{area:.3f}")