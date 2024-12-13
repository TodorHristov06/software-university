start = int(input())
end = int(input())

for number in range(start, end + 1):
    num_str = str(number)
    
    even_sum = int(num_str[0]) + int(num_str[2]) + int(num_str[4])
    
    odd_sum = int(num_str[1]) + int(num_str[3]) + int(num_str[5])
    
    if even_sum == odd_sum:
        print(number, end=" ")