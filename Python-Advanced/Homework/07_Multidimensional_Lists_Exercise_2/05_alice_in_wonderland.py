n = int(input())

matrix = []
alice_pos = ()

for row in range(n):
    line = input().split()
    matrix.append(line)
    if 'A' in line:
        alice_pos = (row, line.index('A'))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

tea_collected = 0
path = []

while tea_collected < 10:
    command = input()

    r, c = alice_pos
    dr, dc = directions[command]
    new_r, new_c = r + dr, c + dc

    matrix[r][c] = '*'

    if not (0 <= new_r < n and 0 <= new_c < n):
        print("Alice didn't make it to the tea party.")
        break

    cell = matrix[new_r][new_c]

    if cell == 'R':
        matrix[new_r][new_c] = '*'
        print("Alice didn't make it to the tea party.")
        break
    elif cell.isdigit():
        tea_collected += int(cell)

    matrix[new_r][new_c] = '*'
    alice_pos = (new_r, new_c)

else:
    print("She did it! She went to the party.")

for row in matrix:
    print(' '.join(row))
