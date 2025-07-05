def print_map(sea_map):
    for row in sea_map:
        print("".join(row))

N = int(input())
sea_map = [list(input()) for _ in range(N)]

ship_row, ship_col = None, None
for r in range(N):
    for c in range(N):
        if sea_map[r][c] == 'S':
            ship_row, ship_col = r, c
            break
    if ship_row is not None:
        break

treasures = sum(row.count('*') for row in sea_map)

durability = 100
charm_used = False

sea_map[ship_row][ship_col] = '.'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == "stop":
        break

    dr, dc = directions[command]
    ship_row = (ship_row + dr) % N
    ship_col = (ship_col + dc) % N

    cell = sea_map[ship_row][ship_col]

    if cell == '.':
        pass

    elif cell == '*':
        treasures -= 1
        sea_map[ship_row][ship_col] = '.'

    elif cell == 'C':
        if not charm_used:
            durability += 25
            if durability > 100:
                durability = 100
            charm_used = True
        sea_map[ship_row][ship_col] = '.'

    elif cell == 'M':
        durability -= 25
        sea_map[ship_row][ship_col] = '.'
        if durability <= 0:
            print(f"Shipwreck! Last known coordinates ({ship_row}, {ship_col})")
            sea_map[ship_row][ship_col] = 'S'
            print(f"Ship Durability: 0")
            if treasures > 0:
                print(f"Unclaimed chests: {treasures}")
            print_map(sea_map)
            exit()

    if treasures == 0:
        print("Yo-ho-ho! All treasure chests collected!")
        sea_map[ship_row][ship_col] = 'S'
        print(f"Ship Durability: {durability}")
        print_map(sea_map)
        exit()

print("Retreat! Some treasures remain unclaimed.")
sea_map[ship_row][ship_col] = 'S'
print(f"Ship Durability: {durability}")
if treasures > 0:
    print(f"Unclaimed chests: {treasures}")
print_map(sea_map)