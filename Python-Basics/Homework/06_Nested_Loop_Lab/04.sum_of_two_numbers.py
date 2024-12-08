interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_number = 0
found = False

for x in range(interval_start, interval_end + 1):
    for y in range(interval_start, interval_end + 1):
        combination_number += 1 
        if x + y == magic_number:
            print(f"Combination N:{combination_number} ({x} + {y} = {magic_number})")
            found = True
            break  
    if found:
        break  

if not found:
    print(f"{combination_number} combinations - neither equals {magic_number}")