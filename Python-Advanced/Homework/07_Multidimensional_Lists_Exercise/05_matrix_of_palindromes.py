rows, cols = map(int, input().split())

for row in range(rows):
    line = []
    for col in range(cols):
        first_last = chr(ord('a') + row)
        middle = chr(ord('a') + row + col)
        palindrome = first_last + middle + first_last
        line.append(palindrome)
    print(' '.join(line))