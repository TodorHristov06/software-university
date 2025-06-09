rows, cols = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum = float('-inf')
best_row = 0
best_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = (
            matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +
            matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +
            matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        )

        if current_sum > max_sum:
            max_sum = current_sum
            best_row = row
            best_col = col

print(f"Sum = {max_sum}")
for i in range(3):
    print(' '.join(str(matrix[best_row + i][best_col + j]) for j in range(3)))
