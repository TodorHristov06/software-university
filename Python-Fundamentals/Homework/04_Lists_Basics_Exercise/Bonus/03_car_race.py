number = list(map(int, input().split()))
half = len(number) // 2
left = number[:half]
right = number[half + 1:][::-1]

right_time = 0
left_time = 0

for i in left:
    if i == 0:
        left_time *= 0.8
    else:
        left_time += i

for i in right:
    if i == 0:
        right_time *= 0.8
    else:
        right_time += i

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")