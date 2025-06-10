n = int(input())

board = [list(input()) for _ in range(n)]

moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

def count_attacks(r, c):
    attacks = 0
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == "K":
                attacks += 1
    return attacks

removed_knights = 0

while True:
    max_attacks = 0
    knight_pos = None

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                current_attacks = count_attacks(row, col)
                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    knight_pos = (row, col)

    if max_attacks == 0:
        break

    r, c = knight_pos
    board[r][c] = "0"
    removed_knights += 1

print(removed_knights)