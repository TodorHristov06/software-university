def perfect_num(number):
    divisor_sum = 0
    for num in range(1, number):
        if number % num == 0:
            divisor_sum += num

    if divisor_sum == number:
        return "We have a perfect number!"
    else:
       return "It's not so perfect."

        
number = int(input())

print(perfect_num(number))