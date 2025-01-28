list_with_numbers = input().split()
opposite_numbers = []

for current_number in list_with_numbers:
    opposite_numbers.append(-int(current_number))

print(opposite_numbers)