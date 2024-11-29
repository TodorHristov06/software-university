from sys import maxsize

input_number = int(input())

max_number = -maxsize
min_number = maxsize

for number in range(1, input_number + 1):
    current_number = int(input())
    
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")