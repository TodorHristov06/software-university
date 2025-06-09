rows, cols = map(int, input().split())
snake = input()

matrix = [['' for _ in range(cols)] for _ in range(rows)]

snake_index = 0
snake_length = len(snake)

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = snake[snake_index % snake_length]
            snake_index += 1
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = snake[snake_index % snake_length]
            snake_index += 1

for row in matrix:
    print(''.join(row))