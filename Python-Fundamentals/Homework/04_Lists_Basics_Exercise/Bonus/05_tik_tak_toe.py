field = [list(map(int, input().split())) for _ in range(3)]

for row in field:
    if row[0] == row[1] == row[2] and row[0] != 0:
        if row[0] == 1:
            print("First player won")
        else:
            print("Second player won")
        exit()

for col in range(3):
    if field[0][col] == field[1][col] == field[2][col] and field[0][col] != 0:
        if field[0][col] == 1:
            print("First player won")
        else:
            print("Second player won")
        exit()

if field[0][0] == field[1][1] == field[2][2] and field[0][0] != 0:
    if field[0][0] == 1:
        print("First player won")
    else:
        print("Second player won")
    exit()

if field[0][2] == field[1][1] == field[2][0] and field[0][2] != 0:
    if field[0][2] == 1:
        print("First player won")
    else:
        print("Second player won")
    exit()

print("Draw!")
