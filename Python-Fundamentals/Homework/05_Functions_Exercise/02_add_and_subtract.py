# def sum_numbers(number):
#     return number[0] + number[1]
# def subtract(sum_number, number):
#     return sum_number - number[2]

# number = [int(input()) for _ in range(3)]
# sum_number = sum_numbers(number)

# print(subtract(sum_number, number))

def sum_numbers(a, b):
    return a + b

def subtract(sum_result, c):
    return sum_result - c

def add_and_subtract(a, b, c):
    sum_result = sum_numbers(a, b)
    return subtract(sum_result, c)

number1 = int(input())
number2 = int(input())
number3 = int(input())

print(add_and_subtract(number1, number2, number3))
