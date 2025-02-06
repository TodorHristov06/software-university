from math import floor

def distance(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

def print_line(x1, y1, x2, y2):
    if distance(x1, y1, 0, 0) <= distance(x2, y2, 0, 0):
        print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
x4, y4 = float(input()), float(input())

line_1 = distance(x1, y1, 0, 0) + distance(x2, y2, 0, 0)
line_2 = distance(x3, y3, 0, 0) + distance(x4, y4, 0, 0)

if line_1 >= line_2:
    print_line(x1, y1, x2, y2)
else:
    print_line(x3, y3, x4, y4)
