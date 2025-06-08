from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

honey = 0

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 0,
}

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(operators[symbols[0]](bees[0], nectar[-1]))
        nectar.pop()
        bees.popleft()
        symbols.popleft()
    else:
        nectar.pop()
print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
