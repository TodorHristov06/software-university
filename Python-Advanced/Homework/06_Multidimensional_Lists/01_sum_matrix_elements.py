row, col = map(int, input().split(", "))
matrix = []
total_sum = 0

for _ in range(row):
    row_data = list(map(int, input().split(", ")))
    total_sum += sum(row_data)
    matrix.append(row_data)

print(total_sum)
print(matrix)