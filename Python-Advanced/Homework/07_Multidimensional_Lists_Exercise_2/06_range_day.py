SIZE = 5
matrix = []
my_position = []
targets = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

directions = {"down": (1, 0), "up": (-1, 0), "right": (0, 1), "left": (0, -1)}
targets_down = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == "shoot":
        r = my_position[0] + directions[command[1]][0]
        c = my_position[1] + directions[command[1]][1]
        while 0 <= r < SIZE and 0 <= c < SIZE:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets -= 1
                targets_down.append([r, c])
                break
            r += directions[command[1]][0]
            c += directions[command[1]][1]
    
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == "move":
        r = my_position[0] + directions[command[1]][0] * int(command[2])
        c = my_position[1] + directions[command[1]][1] * int(command[2])
        if 0 <= r < SIZE and 0 <= c < SIZE and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in targets_down]