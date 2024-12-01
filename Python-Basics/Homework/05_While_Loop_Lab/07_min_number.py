from sys import maxsize

value = input()
min_number = maxsize

while value != 'Stop':
    if int(value) < min_number:
        min_number = int(value)
    value = input()

print(min_number)