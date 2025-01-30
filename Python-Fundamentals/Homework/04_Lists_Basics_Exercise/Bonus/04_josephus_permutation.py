number_of_soldiers = list(map(int, input().split()))
k = int(input())

result = []
index = 0

while number_of_soldiers:
    index = (index + k - 1) % len(number_of_soldiers)
    result.append(number_of_soldiers.pop(index))

print(f"[{','.join(map(str, result))}]")