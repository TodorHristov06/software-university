clothes = list(map(int, input().split()))
capacity = int(input())

current = 0
racks = 1

for piece in clothes[::-1]:
    if current + piece <= capacity:
        current += piece
    else:
        racks += 1
        current = piece

print(racks)
