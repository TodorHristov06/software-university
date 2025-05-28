numbers = tuple(map(float, input().split()))

data = {}
for num in numbers:
    data[num] = numbers.count(num)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")