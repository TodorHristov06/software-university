number = int(input())
binary_digit = int(input())

count = 0

while number > 0:
    leftover = number % 2

    if binary_digit == leftover:
        count += 1
    number //= 2

print(count)