numbers = list(map(int, input().split()))
command = input().split()

while command[0] != "Finish":
    if command[0] == "Add":
        numbers.append(int(command[1]))
    elif command[0] == "Remove":
        if int(command[1]) in numbers:
            numbers.remove(int(command[1]))
    elif command[0] == "Replace":
        value = int(command[1])
        replacement = int(command[2])
        if value in numbers:
            index = numbers.index(value)
            numbers[index] = replacement
    elif command[0] == "Collapse":
        value = int(command[1])
        numbers = [number for number in numbers if number >= value]

    command = input().split()

print(" ".join(map(str, numbers)))