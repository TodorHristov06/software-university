def func_div(number):
    result = 1
    for current_number in range(1, number + 1):
        result *= current_number
    return result

first_number = int(input())
second_number = int(input())

first_factorial = func_div(first_number)
second_factorial = func_div(second_number)

print(f"{first_factorial / second_factorial:.2f}")