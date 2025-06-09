rows, cols = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()

    if parts[0] != "swap" or len(parts) != 5:
        print("Invalid input!")
        continue

    try:
        row1, col1, row2, col2 = map(int, parts[1:])

        if (0 <= row1 < rows and 0 <= col1 < cols and
            0 <= row2 < rows and 0 <= col2 < cols):
            
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            for row in matrix:
                print(' '.join(row))
        else:
            print("Invalid input!")
    except ValueError:
        print("Invalid input!")