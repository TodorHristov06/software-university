n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_diagonal_sum = 0
for i in range(n):
    primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)
