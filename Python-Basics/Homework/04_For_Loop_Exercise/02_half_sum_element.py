import sys

input_number = int(input())

sum_numbers = 0
max_num = -sys.maxsize

for _ in range(0, input_number):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    sum_numbers += current_number

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f'Sum = {max_num}')
else:
    print("No")
    print(f'Diff = {abs(max_num - (sum_numbers - max_num))}')