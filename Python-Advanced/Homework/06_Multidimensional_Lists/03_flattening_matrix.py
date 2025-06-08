row = int(input())
matrix = []

for _ in range(row):
    col = input().split(", ")
    for num in col:
        matrix.append(int(num))

print(matrix)