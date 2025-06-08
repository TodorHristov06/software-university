n = int(input())
matrix = []

for _ in range(n):
    row = input()
    matrix.append(row)

symbol = input()

found = False
for row_index in range(n):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == symbol:
            print(f"({row_index}, {col_index})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
