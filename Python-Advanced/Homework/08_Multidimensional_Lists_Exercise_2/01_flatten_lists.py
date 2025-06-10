line = input()

parts = [part.strip() for part in line.split('|')][::-1]

result = []

for group in parts:
    if group:
        numbers = group.split()
        result.extend(numbers)

print(' '.join(result))