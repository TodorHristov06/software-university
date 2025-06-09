rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]

primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(rows)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))