rows, cols = map(int, input().split(", "))
matrix = []

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

max_sum = None
top_left_row = 0
top_left_col = 0

for r in range(rows - 1):
    for c in range(cols - 1):
        current_sum = (matrix[r][c] + matrix[r][c+1] +
                       matrix[r+1][c] + matrix[r+1][c+1])
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            top_left_row = r
            top_left_col = c

print(matrix[top_left_row][top_left_col], matrix[top_left_row][top_left_col+1])
print(matrix[top_left_row+1][top_left_col], matrix[top_left_row+1][top_left_col+1])
print(max_sum)
