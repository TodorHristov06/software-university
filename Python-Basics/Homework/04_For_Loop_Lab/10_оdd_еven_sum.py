input_number = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, input_number + 1):
    current_number = int(input())
    
    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")