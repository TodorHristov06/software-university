number = int(input())
unfiltered = []
filtered = []
for _ in range(number):
    data = int(input())
    unfiltered.append(data)

command = input()

if command == "even":
    for number in unfiltered:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in unfiltered:
        if number % 2 != 0:
            filtered.append(number)
elif command == "negative":
    for number in unfiltered:
        if number < 0:
            filtered.append(number)
elif command == "positive":
    for number in unfiltered:
        if number >= 0:
            filtered.append(number)
print(filtered)