def is_in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

presents = int(input())
n = int(input())
matrix = []
santa_pos = ()
nice_kids_total = 0

for i in range(n):
    row = input().split()
    for j in range(n):
        if row[j] == "S":
            santa_pos = (i, j)
        elif row[j] == "V":
            nice_kids_total += 1
    matrix.append(row)

nice_kids_with_presents = 0

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    delta_r, delta_c = directions[command]
    r, c = santa_pos
    new_r, new_c = r + delta_r, c + delta_c

    if not is_in_range(new_r, new_c, n):
        continue

    matrix[r][c] = "-"

    if matrix[new_r][new_c] == "V":
        presents -= 1
        nice_kids_with_presents += 1
    elif matrix[new_r][new_c] == "C":
        for dir in directions.values():
            adj_r, adj_c = new_r + dir[0], new_c + dir[1]
            if is_in_range(adj_r, adj_c, n):
                if matrix[adj_r][adj_c] in ("V", "X"):
                    presents -= 1
                    if matrix[adj_r][adj_c] == "V":
                        nice_kids_with_presents += 1
                    matrix[adj_r][adj_c] = "-"
                    if presents == 0:
                        break
    santa_pos = (new_r, new_c)
    matrix[new_r][new_c] = "S"

    if presents == 0:
        break

if presents == 0 and nice_kids_with_presents < nice_kids_total:
    print("Santa ran out of presents!")

for row in matrix:
    print(" ".join(row))

if nice_kids_with_presents == nice_kids_total:
    print(f"Good job, Santa! {nice_kids_total} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_total - nice_kids_with_presents} nice kid/s.")
