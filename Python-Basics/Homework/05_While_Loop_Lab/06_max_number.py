from sys import maxsize

value = input()
max_number = -maxsize

while value != 'Stop':
    if int(value) > max_number:
        max_number = int(value)
    value = input()

print(max_number)