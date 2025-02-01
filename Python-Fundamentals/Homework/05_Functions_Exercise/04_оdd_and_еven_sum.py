# def sum_of_even(number):
#     even_sum = 0
#     for char in number:
#         digit = int(char)
#         if digit % 2 == 0:
#             even_sum += digit
#     return even_sum

# def sum_of_odd(number):
#     odd_sum = 0
#     for char in number:
#         digit = int(char)
#         if digit % 2 != 0:
#             odd_sum += digit
#     return odd_sum

# number = input()

# print(f"Odd sum = {sum_of_odd(number)}, Even sum = {sum_of_even(number)}")

def sum_by_condition(number: str, condition) -> int:
    return sum(int(char) for char in number if condition(int(char)))

number = input()

odd_num = sum_by_condition(number, lambda char: char % 2 != 0)
even_num = sum_by_condition(number, lambda char: char % 2 == 0)

print(f"Odd sum = {odd_num}, Even sum = {even_num}")