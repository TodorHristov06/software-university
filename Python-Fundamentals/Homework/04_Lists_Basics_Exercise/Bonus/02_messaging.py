numbers = list(map(int, input().split()))
message = list(input())
result = []

for number in numbers:
    index = sum(map(int, str(number)))
    index = index % len(message)
    result.append(message.pop(index))

print("".join(result))